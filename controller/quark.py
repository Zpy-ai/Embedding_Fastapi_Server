from http import HTTPStatus
import dashscope

# 检查操作状态的函数
def check_status(component, operation):
    return component.status_code == HTTPStatus.OK



# 创建Web搜索助手
def create_search_assistant():
    return dashscope.Assistants.create(
    model='qwen-max',
    name='Web Search Pro',
    description='专注于网络信息检索的AI助手',
    instructions='''使用夸克搜索工具获取互联网上的最新信息、百科知识、新闻等各类内容，
    并以清晰、简洁的方式总结和呈现搜索结果。''',
    tools=[
        {'type': 'quark_search', 'description': '用于查找互联网上的最新信息、百科知识、新闻等各类内容。'}
    ]
)