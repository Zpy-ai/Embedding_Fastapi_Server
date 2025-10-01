from typing import List, Literal
from pydantic import BaseModel

# bge-m3 embedding模型请求和响应数据定义
class BgeEmbeddingRequest(BaseModel):
    texts: List[str]
    model: Literal[
        "bge-m3"
    ]


class BgeEmbeddingResponse(BaseModel):
    data: list
    model: str
    usage: dict


# bge-reranker-v2-m3 请求和响应模型
class BgeRerankeRequest(BaseModel):
    query: str
    texts: List[str]
    #normalize: Optional[bool] = Field(False, description="是否对分数进行归一化处理")
    num: int
    model: Literal[
        "bge-reranker-v2-m3"
    ]



class BgeRerankeResponse(BaseModel):
    TOP: list
    data: list
    model: str

# jina-clip-v2相关请求和响应数据定义
class ClipTextgRequest(BaseModel):
    texts: List[str]
    model: Literal[
        "jina-clip-v2"
    ]


class ClipTextResponse(BaseModel):
    data: list
    model: str
    usage: dict

class ClipImgRequest(BaseModel):  # CLIP图片请求数据定义
    b64_imgs: List[str]  # Base64格式的图片
    model: Literal[
        "jina-clip-v2"
    ]


class ClipImgReqponse(BaseModel):  # CLIP图片返回数据定义
    data: List
    model: str


# jina-reranker-m0 请求和响应数据定义
class JinaRequest(BaseModel):
    query: str  # 查询文本
    texts: List[str]
    b64_imgs: List[str] # 图片列表，base64编码
    num: int
    model: Literal[
        "jina-reranker-m0"
    ]


class JinaResponse(BaseModel):
    TOP: list # 前5个结果
    data: list
    model: str
    usage: dict

# web请求模型
class SearchRequest(BaseModel):
    query: str
    tools: Literal ["quark_search"]


# web响应模型
class SearchResponse(BaseModel):
    response: str
    tools_used: str