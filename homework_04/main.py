"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
import aiohttp

from jsonplaceholder_requests import fetch_data, USERS_DATA_URL, POSTS_DATA_URL
from models import async_engine, Base, User, Post, Session


async def fetch_users_data():
    async with aiohttp.ClientSession():
        users_data = []
        data = await fetch_data(USERS_DATA_URL)
        for user in data:
            users_data.append({x: user.get(x) for x in ("name", "username", "email")})
    return users_data


async def fetch_posts_data():
    async with aiohttp.ClientSession():
        posts_data = []
        data = await fetch_data(POSTS_DATA_URL)
        for post in data:
            posts_data.append({x: post.get(x) for x in ("userId", "title", "body")})
    return posts_data


async def create_tables(conn):
    await conn.run_sync(Base.metadata.drop_all)
    await conn.run_sync(Base.metadata.create_all)


async def create_users(session, user):
    user = User(name=user.get("name"), username=user.get("username"), email=user.get("email"))
    session.add(user)


async def create_posts(session, post):
    post = Post(user_id=post.get("userId"), title=post.get("title"), body=post.get("body"))
    session.add(post)


async def async_main():
    async with async_engine.begin() as conn:
        await create_tables(conn)

    async with Session() as session:
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data()
        )
        for user in users_data:
            await create_users(session, user)
        for post in posts_data:
            await create_posts(session, post)
        await session.commit()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
