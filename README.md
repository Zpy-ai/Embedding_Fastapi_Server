# FastAPI-based Local Large Model Interface

## 中文版 | [English Version](#english-version)

## 一、简介
一个基于FastAPI的大模型接口项目，它集成文本与多模态大模型，支持批量文本、base64图片输入，返回向量数据、相关度排序、模型信息及token使用统计；配置CORS中间件允许全来源跨域请求，设置请求头密钥增强安全性。
## 二、项目结构
```plaintext
modelsAPI8.0/
├─ api/           # 存放API路由和相关配置的目录
│  ├─ config.py   # 配置文件，定义了API密钥
│  ├─ router.py   # 总路由文件，包含所有子路由
│  ├─ jinaranker.py # Jina重排序器的API接口
│  ├─ bgeranker.py # BGE重排序器的API接口
│  ├─ embedding.py # BGE文本嵌入的API接口
│  ├─ clip.py     # CLIP模型的文本和图像嵌入的API接口
│  ├─ quarkweb.py  # 夸克Web搜索API接口
│  ├─ schemas.py  # 定义API请求和响应的数据结构
│  └─ health.py   # 健康检查的API接口
├─ common/        # 存放通用工具和模型加载函数的目录
│  ├─ logger.py   # 日志配置文件
│  └─ bot.py      # 模型加载函数，包括BGE、Jina等模型
├─ controller/    # 存放业务逻辑处理函数的目录
│  ├─ embedding.py # 处理嵌入向量的功能函数
│  ├─ clip.py     # CLIP模型的业务逻辑处理函数
│  ├─ reranker.py # 重排序器的业务逻辑处理函数
│  └─ quark.py    # 夸克Web搜索业务逻辑处理函数
├─ utils/         # 存放实用工具函数的目录
│  ├─ gc.py       # 回收显存的工具函数
│  └─ convert.py  # 处理Base64编码图像转换的工具函数
├─ main.py        # 项目的入口文件，启动FastAPI应用
├─ requirements.txt # 项目依赖的Python包列表
├─ logs/          # 日志目录
└─ README.md      # 项目说明文档
```

## 三、环境配置
### 3.1 依赖安装
项目依赖的 Python 包列表在requirements.txt文件中，可使用以下命令安装所有依赖：
pip install -r requirements.txt

### 3.2 API 密钥配置
在 `api/config.py` 文件中配置 API 密钥，默认值为 `your_api_key`，请根据实际需求修改：

```python
from os import getenv

sk_key = getenv("sk-key", "your_api_key")
```

## 四、使用指南

### 4.1 安装依赖
```bash
pip install -r requirements.txt
```

### 4.2 启动服务
在项目根目录下，运行 main.py 文件：
```bash
python main.py
```

### 4.3 访问接口
服务启动后，默认运行在 `http://localhost:8000`，可以通过以下方式访问接口：
- 直接访问API端点
- 使用Swagger文档：`http://localhost:8000/docs`
- 使用Redoc文档：`http://localhost:8000/redoc`
## 五、接口说明

### 5.1 BGE-M3 文本嵌入接口

将文本转换为高维向量表示，支持多语言文本嵌入。

```javascript
http://localhost:8000/api/v1/embedding
```

### 5.2 BGE-Reranker-v2-M3 重排序接口

根据查询文本对候选文本进行相关性重排序。

```javascript
http://localhost:8000/api/v2/reranker
```

### 5.3 Jina-CLIP-v2 多模态接口

支持文本和图像的向量化表示，包含两个子接口：

#### 5.3.1 文本向量化接口
```javascript
http://localhost:8000/api/v2/clip/text
```

#### 5.3.2 图像向量化接口（Base64格式）
```javascript
http://localhost:8000/api/v2/clip/img
```

### 5.4 Jina-Reranker-M0 多模态重排序接口

支持文本和图像的混合重排序，包含两个子接口：

#### 5.4.1 文本输入重排序接口
```javascript
http://localhost:8000/api/v1/text/reranker
```

#### 5.4.2 图像输入重排序接口（Base64格式）
```javascript
http://localhost:8000/api/v1/img/reranker
```

### 5.5 健康检查接口

检查服务运行状态和接口可用性。

```javascript
http://localhost:8000/api/v1/apihealth
```

### 5.6 夸克Web搜索接口

提供互联网信息检索服务，支持实时网络搜索。

```javascript
http://localhost:8000/api/v3/plugins/webSearch
```

## 六、请求地址汇总

| 接口功能 | 请求地址 | 版本 |
|---------|---------|------|
| 文本嵌入 | `http://localhost:8000/api/v1/embedding` | v1 |
| 文本重排序 | `http://localhost:8000/api/v2/reranker` | v2 |
| 文本向量化 | `http://localhost:8000/api/v2/clip/text` | v2 |
| 图像向量化 | `http://localhost:8000/api/v2/clip/img` | v2 |
| 文本重排序 | `http://localhost:8000/api/v1/text/reranker` | v1 |
| 图像重排序 | `http://localhost:8000/api/v1/img/reranker` | v1 |
| Web搜索 | `http://localhost:8000/api/v3/plugins/webSearch` | v3 |
| 健康检查 | `http://localhost:8000/api/v1/apihealth` | v1 |

## 七、请求示例

### 7.1 文本嵌入接口 (BGE-M3)

v1/[embedding](http://10.8.130.31:6008/api/v1/bgeembedding)接口

```json
{
  "texts": [
    "你好我是zpy"
  ],
  "model": "bge-m3"
}
```

### 7.2 文本重排序接口 (BGE-Reranker-v2-M3)

```json
{
    "query":"你好我是zpy",
    "texts": [
        "你好我是zpy",
        "你好我是zy"
  ],
  "model": "bge-reranker-v2-m3",
    "num": 5
}
```

### 7.3 文本向量化接口 (Jina-CLIP-v2)

```json
{
    "texts": [ "غروب جميل على الشاطئ",
    "海滩上美丽的日落",
    "Un beau coucher de soleil sur la plage",
    "Ein wunderschöner Sonnenuntergang am Strand",
    "Ένα όμορφο ηλιοβασίλεμα πάνω από την παραλία",
    "समुद्र तट पर एक खूबसूरत सूर्यास्त",
    "Un bellissimo tramonto sulla spiaggia",
    "浜辺に沈む美しい夕日",
    "해변 위로 아름다운 일몰"
    ],
    "model": "jina-clip-v2"
}
```

### 7.4 图像向量化接口 (Jina-CLIP-v2)

```json
{
    "b64_imgs": ["R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7"],
    "model": "jina-clip-v2"
}
```

### 7.5 多模态文本重排序接口 (Jina-Reranker-M0)

```json
{
    "query": "slm markdown",
    "texts": [
        "We present ReaderLM-v2, a compact 1.5 billion parameter language model designed for efficient web content extraction. Our model processes documents up to 512K tokens, transforming messy HTML into clean Markdown or JSON formats with high accuracy -- making it an ideal tool for grounding large language models. The models effectiveness results from two key innovations: (1) a three-stage data synthesis pipeline that generates high quality, diverse training data by iteratively drafting, refining, and critiquing web content extraction; and (2) a unified training framework combining continuous pre-training with multi-objective optimization. Intensive evaluation demonstrates that ReaderLM-v2 outperforms GPT-4o-2024-08-06 and other larger models by 15-20% on carefully curated benchmarks, particularly excelling at documents exceeding 100K tokens, while maintaining significantly lower computational requirements.",
        "数据提取么？为什么不用正则啊，你用正则不就全解决了么？",
        "slm markdown"
        ],
    "b64_imgs": [
        "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"
    ],
    "num": 5,
    "model": "jina-reranker-m0"
}
```

### 7.6 多模态图像重排序接口 (Jina-Reranker-M0)

```json
{
    "query": "iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAA7VBMVEX///8AAABONC780K49Wv5gfYu8vLwiIiIAvNRHLypceJ5hfoc4Vf//1bL8/PxSbsCCgoLk5OQpKSlOQDXctpgZEA9AXv8SG0sGCRorHRocKnY4U+sKDQ7rwqISGBssOkE+Pj5fX19MY29ZdIF1YFGHcF68m4EjLTKSkpInOqIcJSndzbU9UFlcv87DyrvrzrF1wcpOTk6jo6OixsE7MCg4JSHLy8skNZLNqo4EBQ9kU0VZSj0uJh93d3cyMjKihnBvamZca3KoqbI8R5YaLI41R3omM1lNZ7EAAEEbIy46TGcwPk8jEQyIw8eZjobFTeMIAAAFHUlEQVR4nO3da0PaOhwG8CGOHqYwKqBjFKQ6sJt63Biy6Siw+/18/48zSP7FhqU5XNr04vP4igRCfmsX2jSFBw+2TTm0bN2V7ePkQooTt2SWvhGOxejHLZml3w4H0wYm5ACTWExIA0A8GNN+5c/YYn2pF7dNh7dX0YvpyP5hG8WdLdPgDdnAAANM6jD1dGMa10K2tXiYTp9HzxmBh9l6U8gxlI4JDDDAABNRyibLsFNnCRtzzZutc8x4yN8tqhG6cGDNQ4qwLV6KtGnYe1kHhagwRkif9StheAxggAEGmJRidmiyhj5vDjosoc+qa8JQ6sIWCn0CSiumCAwwwNxfzA5N+tQzgaE0gAEGGGBCU5hDFmfUYNFpCR/jjFkGWjdJVJgKb1DvJgEGGGCAiQXjzeEXpaVi6GJuUVrppRgrRnZ4cJ2TpeFhpLU5oaFYMEU5xgIGGGDuDybXEMMLB5Meyy11VKgcUSVlwkstek7oszPrYKS5bZVYurLKwduSPzVpCwnCvKuV8vMEYfJ3AQaYLGBc3uCvjTHVBGEKlXmcqWoBoxxT7bJMWry/va4kk5qIoeJRRBi6japg5IJXAMkx3RbLoqstWfJieGGtGhGGopwEDMDkS/mNUmolEbNpgAEmuxi+OoTmAKxB1Z8Jde2KR97vK1ktYSy6RUjTchNxaeWoV/OHht3z35fzvPxXannNKi/FSsIYfb5UM/Tlp3KMuOh1UBOO52lgPr/8h0WOeckrX0sxelc1/YWR9BcYYO43ZkeBGaUM482biHNB72hypZUujBcR86wlDMapx8h6CgwwwGQTQ3M12cCIVytSjskBAwww/4ORXqBMKWZo80hNSszVb9mchbIyaox3B+14bUz+6pxFPtd0LquMGkORf+2EGrN+gAEGmIRijANf2qnGlIcFf1wrVIx3gfbZSAtmKfRlbeFhhL1XN6YNDDDRY7L0f8ZZDM3B07MB/ZZmae2MXszQYStr/lNNnMstrZ4stKzRqPAMtWI8Ez8ukF/SCNihxLU+YjR9vZESI7/YFIAZAAMMMMuLGlRRYsZxYkyXzdxMxeUmyvSmdnCmcWJo6sZ0qyvHNVVJwJfRl23FrrMUOwH9Vcacro6JdU9aJcAkNaa9OsZOOqbssrvtO3T1oz4a+DKi5YJGhz3JTfoAQFM3Q9rbbsXDe7qzaUpPSjrGC52ydcXPfLqxIQk/AbJOPIx4OAZM/AEmqcniACAfmlOKkQeYGANMUgNMjFFORzjts8C0HeVLY8HYwkVnMcbJQ0VOVK/U+ysnC4xqT7pQYS5UrwQGGGASjaHfJbVz7XlokaPV9sdSj2ZLT/a3MMPo/N1Ts+KyS6fvT1iOeV/OToScqjCn4nPPuOWYP3rPGncrmn6yhdZoUn8vOOZY2X0l7ZhjaM885a1ruj7jrTeLFqP5x3SAASaS8CFzhrmZJToMa32GiXSENvk6xg8fP72Z5dNjns83rC9fvj7eMF+/sAZuPtNj3vrHD/zdotpABb4DfGsesuzuz7P7/Akrfdrkj9fObvMpa+DJc2qQt978xt8t4ltOjpq7vhzeYTbMAnMolB6x0qjvnwEGGGCAAQYYYIABJjmY74+E/ODnMz8fbZyfrAHrh1j6XQvmxemeP4uTs70Nszg5E0tfaMIIJ4phn2l6pcAAAwwwwAADDDBRYvYWfz6Mr3Bv6U9V4MP46jVhMnXUfCTMkN9NnG82b76/vzRx7rWLkzNggAEGmCxg/gAcTwKRD+vGjgAAAABJRU5ErkJggg==",
    "texts": [
        "We present ReaderLM-v2, a compact 1.5 billion parameter language model designed for efficient web content extraction. Our model processes documents up to 512K tokens, transforming messy HTML into clean Markdown or JSON formats with high accuracy -- making it an ideal tool for grounding large language models. The models effectiveness results from two key innovations: (1) a three-stage data synthesis pipeline that generates high quality, diverse training data by iteratively drafting, refining, and critiquing web content extraction; and (2) a unified training framework combining continuous pre-training with multi-objective optimization. Intensive evaluation demonstrates that ReaderLM-v2 outperforms GPT-4o-2024-08-06 and other larger models by 15-20% on carefully curated benchmarks, particularly excelling at documents exceeding 100K tokens, while maintaining significantly lower computational requirements.",
        "数据提取么？为什么不用正则啊，你用正则不就全解决了么？"],
    "b64_imgs": ["iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAA7VBMVEX///8AAABONC780K49Wv5gfYu8vLwiIiIAvNRHLypceJ5hfoc4Vf//1bL8/PxSbsCCgoLk5OQpKSlOQDXctpgZEA9AXv8SG0sGCRorHRocKnY4U+sKDQ7rwqISGBssOkE+Pj5fX19MY29ZdIF1YFGHcF68m4EjLTKSkpInOqIcJSndzbU9UFlcv87DyrvrzrF1wcpOTk6jo6OixsE7MCg4JSHLy8skNZLNqo4EBQ9kU0VZSj0uJh93d3cyMjKihnBvamZca3KoqbI8R5YaLI41R3omM1lNZ7EAAEEbIy46TGcwPk8jEQyIw8eZjobFTeMIAAAFHUlEQVR4nO3da0PaOhwG8CGOHqYwKqBjFKQ6sJt63Biy6Siw+/18/48zSP7FhqU5XNr04vP4igRCfmsX2jSFBw+2TTm0bN2V7ePkQooTt2SWvhGOxejHLZml3w4H0wYm5ACTWExIA0A8GNN+5c/YYn2pF7dNh7dX0YvpyP5hG8WdLdPgDdnAAANM6jD1dGMa10K2tXiYTp9HzxmBh9l6U8gxlI4JDDDAABNRyibLsFNnCRtzzZutc8x4yN8tqhG6cGDNQ4qwLV6KtGnYe1kHhagwRkif9StheAxggAEGmJRidmiyhj5vDjosoc+qa8JQ6sIWCn0CSiumCAwwwNxfzA5N+tQzgaE0gAEGGGBCU5hDFmfUYNFpCR/jjFkGWjdJVJgKb1DvJgEGGGCAiQXjzeEXpaVi6GJuUVrppRgrRnZ4cJ2TpeFhpLU5oaFYMEU5xgIGGGDuDybXEMMLB5Meyy11VKgcUSVlwkstek7oszPrYKS5bZVYurLKwduSPzVpCwnCvKuV8vMEYfJ3AQaYLGBc3uCvjTHVBGEKlXmcqWoBoxxT7bJMWry/va4kk5qIoeJRRBi6japg5IJXAMkx3RbLoqstWfJieGGtGhGGopwEDMDkS/mNUmolEbNpgAEmuxi+OoTmAKxB1Z8Jde2KR97vK1ktYSy6RUjTchNxaeWoV/OHht3z35fzvPxXannNKi/FSsIYfb5UM/Tlp3KMuOh1UBOO52lgPr/8h0WOeckrX0sxelc1/YWR9BcYYO43ZkeBGaUM482biHNB72hypZUujBcR86wlDMapx8h6CgwwwGQTQ3M12cCIVytSjskBAwww/4ORXqBMKWZo80hNSszVb9mchbIyaox3B+14bUz+6pxFPtd0LquMGkORf+2EGrN+gAEGmIRijANf2qnGlIcFf1wrVIx3gfbZSAtmKfRlbeFhhL1XN6YNDDDRY7L0f8ZZDM3B07MB/ZZmae2MXszQYStr/lNNnMstrZ4stKzRqPAMtWI8Ez8ukF/SCNihxLU+YjR9vZESI7/YFIAZAAMMMMuLGlRRYsZxYkyXzdxMxeUmyvSmdnCmcWJo6sZ0qyvHNVVJwJfRl23FrrMUOwH9Vcacro6JdU9aJcAkNaa9OsZOOqbssrvtO3T1oz4a+DKi5YJGhz3JTfoAQFM3Q9rbbsXDe7qzaUpPSjrGC52ydcXPfLqxIQk/AbJOPIx4OAZM/AEmqcniACAfmlOKkQeYGANMUgNMjFFORzjts8C0HeVLY8HYwkVnMcbJQ0VOVK/U+ysnC4xqT7pQYS5UrwQGGGASjaHfJbVz7XlokaPV9sdSj2ZLT/a3MMPo/N1Ts+KyS6fvT1iOeV/OToScqjCn4nPPuOWYP3rPGncrmn6yhdZoUn8vOOZY2X0l7ZhjaM885a1ruj7jrTeLFqP5x3SAASaS8CFzhrmZJToMa32GiXSENvk6xg8fP72Z5dNjns83rC9fvj7eMF+/sAZuPtNj3vrHD/zdotpABb4DfGsesuzuz7P7/Akrfdrkj9fObvMpa+DJc2qQt978xt8t4ltOjpq7vhzeYTbMAnMolB6x0qjvnwEGGGCAAQYYYIABJjmY74+E/ODnMz8fbZyfrAHrh1j6XQvmxemeP4uTs70Nszg5E0tfaMIIJ4phn2l6pcAAAwwwwAADDDBRYvYWfz6Mr3Bv6U9V4MP46jVhMnXUfCTMkN9NnG82b76/vzRx7rWLkzNggAEGmCxg/gAcTwKRD+vGjgAAAABJRU5ErkJggg=="
    ],
    "num": 5,
    "model": "jina-reranker-m0"
}
```

## 八、请求参数

**Body**参数

| 名称 | 类型 | 必填 | 说明 |
|----|----|----|----|
| query | str | 是 | 要搜索的关键词，支持传入一个关键词，类型为str |
| texts | list | 是 | 要搜索的文本，至少输入一个，query与list列表中每一个文本计算相关度分数 |
| b64_imgs | list | 是 | 输入base64格式的图片 |
| num | int | 是 | 返回的相关度文本个数，按照相关度从大到小 |
| model | str | 是 | 输入需要使用的模型名字 |

**参数示例一**：输入文本，传入列表

```json
{
    "texts": [ "غروب جميل على الشاطئ",
    "海滩上美丽的日落",
    "Un beau coucher de soleil sur la plage",
    "Ein wunderschöner Sonnenuntergang am Strand",
    "Ένα όμορφο ηλιοβασίλεμα πάνω από την παραλία",
    "समुद्र तट पर एक खूबसूरत सूर्यास्त",
    "Un bellissimo tramonto sulla spiaggia",
    "浜辺に沈む美しい夕日",
    "해변 위로 아름다운 일몰"
    ],
    "model": "jina-clip-v2"
}
```

**参数示例二**：输入base64图片，传入列表(注意第二行最后有一个逗号)

```json
{
    "b64_imgs": ["R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7"],
    "model": "jina-clip-v2"
}
```

**参数示例三**： 输入文本和图片，传入列表

```json
{
    "query": "Organic skincare products for sensitive skin",
    "texts": [
        "Organic skincare for sensitive skin with aloe vera and chamomile.",
    "New makeup trends focus on bold colors and innovative techniques",
    "Bio-Hautpflege für empfindliche Haut mit Aloe Vera und Kamille",
    "Neue Make-up-Trends setzen auf kräftige Farben und innovative Techniken",
    "Cuidado de la piel orgánico para piel sensible con aloe vera y manzanilla",
    "Las nuevas tendencias de maquillaje se centran en colores vivos y técnicas innovadoras",
    "针对敏感肌专门设计的天然有机护肤产品",
    "新的化妆趋势注重鲜艳的颜色和创新的技巧",
    "敏感肌のために特別に設計された天然有機スキンケア製品",
    "新しいメイクのトレンドは鮮やかな色と革新的な技術に焦点を当てています"
    ],
    "b64_imgs": [
       "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"
    ],
    "num": 5,
    "model": "jina-clip-v2"
}
```


## 九、返回值说明

### 通用返回字段

| 字段名 | 类型 | 说明 | 示例值 |
|--------|------|------|--------|
| model | str | 所使用模型的名字 | `"bge-m3"` |
| usage | dict | 输入文本令牌数和总令牌数 | `{"prompt_tokens": 1, "total_tokens": 518}` |
| data | list | 返回的具体数据 | 见下方详细说明 |

### WebSearchData 字段说明

| 字段名 | 类型 | 说明 | 示例值 |
|--------|------|------|--------|
| embedding | list | 向量值 | `[0.7070459723472595, ...]` |
| index | int | 序号 | `0` |
| score | float | 相关度分数 | `0.7783799171447754` |
| object | str | 数据类型 | `"vector"` |
| model | str | 使用的模型 | `"jina-reranker-m0"` |
| type | str | 类型（文本/图片） | `"text"` 或 `"img"` |
| msg | str | 返回状态 | `"success"` |
| content | str | 文本或base64图片 | `"数据提取么？为什么不用正则啊，你用正则不就全解决了么？"` |

**返回值示例：**

```json
{
    "TOP": [
        [
            {
                "type": "image",
                "content": "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",
                "score": 0.9671133756637573,
                "index": 0
            },
            {
                "type": "text",
                "content": "数据提取么？为什么不用正则啊，你用正则不就全解决了么？",
                "score": 0.6054257750511169,
                "index": 1
            },
            {
                "type": "text",
                "content": "We present ReaderLM-v2, a compact 1.5 billion parameter language model designed for efficient web content extraction. Our model processes documents up to 512K tokens, transforming messy HTML into clean Markdown or JSON formats with high accuracy -- making it an ideal tool for grounding large language models. The models effectiveness results from two key innovations: (1) a three-stage data synthesis pipeline that generates high quality, diverse training data by iteratively drafting, refining, and critiquing web content extraction; and (2) a unified training framework combining continuous pre-training with multi-objective optimization. Intensive evaluation demonstrates that ReaderLM-v2 outperforms GPT-4o-2024-08-06 and other larger models by 15-20% on carefully curated benchmarks, particularly excelling at documents exceeding 100K tokens, while maintaining significantly lower computational requirements.",
                "score": 0.4586881399154663,
                "index": 0
            }
        ]
    ],
    "data": [
        [
            {
                "type": "image",
                "content": "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",
                "score": 0.9671133756637573,
                "index": 0
            },
            {
                "type": "text",
                "content": "数据提取么？为什么不用正则啊，你用正则不就全解决了么？",
                "score": 0.6054257750511169,
                "index": 1
            },
            {
                "type": "text",
                "content": "We present ReaderLM-v2, a compact 1.5 billion parameter language model designed for efficient web content extraction. Our model processes documents up to 512K tokens, transforming messy HTML into clean Markdown or JSON formats with high accuracy -- making it an ideal tool for grounding large language models. The models effectiveness results from two key innovations: (1) a three-stage data synthesis pipeline that generates high quality, diverse training data by iteratively drafting, refining, and critiquing web content extraction; and (2) a unified training framework combining continuous pre-training with multi-objective optimization. Intensive evaluation demonstrates that ReaderLM-v2 outperforms GPT-4o-2024-08-06 and other larger models by 15-20% on carefully curated benchmarks, particularly excelling at documents exceeding 100K tokens, while maintaining significantly lower computational requirements.",
                "score": 0.4586881399154663,
                "index": 0
            }
        ]
    ],
    "model": "jina-reranker-m0",
    "usage": {
        "prompt_tokens": 1,
        "total_tokens": 941
    }
}
```


