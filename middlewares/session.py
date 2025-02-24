from collections.abc import Awaitable, Callable
from typing import Any, Optional

import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from config import DATABASE_URL


class SessionMiddleware(BaseMiddleware):
    pool: Optional[asyncpg.Pool] = None
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        # Создаем пул соединений при первом вызове
        if self.pool is None:
            self.pool = await asyncpg.create_pool(
                DATABASE_URL,
                min_size=5,
                max_size=20
            )
        
        # Получаем соединение из пула
        async with self.pool.acquire() as conn:
            data["session"] = conn
            return await handler(event, data)
    
    @classmethod
    async def close(cls) -> None:
        """Закрыть пул соединений при завершении работы приложения."""
        if cls.pool is not None:
            await cls.pool.close()
            cls.pool = None
