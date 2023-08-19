from ninja import NinjaAPI

from blog.api import router as blog_router


api = NinjaAPI()

api.add_router("/", blog_router)

# TODO 设计注册User和User登录的接口