import pytest
import asyncio
from playwright.async_api import async_playwright, expect


async def test_api_requests():
    async with async_playwright() as p:
        # Create request context
        request_context = await p.request.new_context()

        # 1. GET Request
        get_resp = await request_context.get("https://jsonplaceholder.typicode.com/posts/1")
        assert get_resp.status == 200
        data = await get_resp.json()
        print("GET Title:", data["title"])

        # 2. POST Request
        post_resp = await request_context.post(
            "https://jsonplaceholder.typicode.com/posts",
            data={"title": "foo", "body": "bar", "userId": 1}
        )
        assert post_resp.status == 201
        post_data = await post_resp.json()
        print("POST ID:", post_data["id"])

        # 3. PUT Request
        put_resp = await request_context.put(
            "https://jsonplaceholder.typicode.com/posts/1",
            data={"id": 1, "title": "updated title", "body": "bar", "userId": 1}
        )
        assert put_resp.status == 200
        updated = await put_resp.json()
        print("Updated Title:", updated["title"])

        # 4. DELETE Request
        delete_resp = await request_context.delete("https://jsonplaceholder.typicode.com/posts/1")
        assert delete_resp.status == 200

        # 5. GET with Custom Headers
        custom_resp = await request_context.get(
            "https://httpbin.org/headers",
            headers={"Authorization": "Bearer harsh_dummy_token"}
        )
        assert custom_resp.status == 200
        headers_data = await custom_resp.json()
        print("Authorization Header:", headers_data["headers"]["Authorization"])

        # 6. POST with Form Data
        form_resp = await request_context.post(
            "https://httpbin.org/post",
            form={"username": "abc", "password": "test123"}
        )
        assert form_resp.status == 200
        form_data = await form_resp.json()
        print("Form POST:", form_data["form"])

        # Clean up
        await request_context.dispose()

        print("\n✅ All async API tests completed.")