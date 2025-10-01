import dashscope
from fastapi import Depends, HTTPException, status, APIRouter
import json
from api.schemas import SearchRequest, SearchResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api.config import sk_key
from controller.quark import create_search_assistant, check_status


router = APIRouter()  # 创建子路由

security = HTTPBearer()

# 设置Dashscope API密钥
dashscope.api_key = "sk-139a40229c0e4bd58191a7a2f8c9c8f3"

@router.post("/websearch", summary="7、QuarkSearch", response_model=SearchResponse)
async def search_endpoint(request: SearchRequest ,
                          credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != sk_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization code",
        )
    # 创建搜索助手
    search_assistant = create_search_assistant()
    if not check_status(search_assistant, "助手创建"):
        exit()

    # 2. 创建一个新线程
    thread = dashscope.Threads.create()

    if not check_status(thread, "线程创建"):
        exit()

    # 3. 向线程发送消息（用户查询）
    user_query = request.query
    if not user_query:
        return {"response": "查询内容不能为空", "tools_used": ""}
    message = dashscope.Messages.create(thread.id, content=user_query)

    if not check_status(message, "消息创建"):
        exit()

    # 4. 在线程上运行助手
    run = dashscope.Runs.create(thread.id, assistant_id=search_assistant.id)

    if not check_status(run, "运行创建"):
        exit()

    # 5. 等待运行完成
    print("等待助手处理请求...")
    run = dashscope.Runs.wait(run.id, thread_id=thread.id)

    if check_status(run, "运行完成"):
        print(f"运行完成，状态：{run.status}")
    else:
        exit()

    # 6. 检索并显示助手的响应
    messages = dashscope.Messages.list(thread.id)

    if check_status(messages, "消息检索"):
        if messages.data:
            # 显示最后一条消息的内容（助手的响应）
            last_message = messages.data[0]
            assistant_text = ""
            if hasattr(last_message, 'content') and last_message.content:
                for content_item in last_message.content:
                    if hasattr(content_item, 'text') and hasattr(content_item.text, 'value'):
                        assistant_text += content_item.text.value
            
            # 构建响应
            response = {
                "response": assistant_text,
                "tools_used": "quark_search"
            }
        
        return response
