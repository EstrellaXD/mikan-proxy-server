# 简易版 Mikanani 反代服务

## 运行

```bash
docker run -d \
    -p 6789:6789 \
    -e URL=yourdomian.com \
    --name mikanani-proxy \
    estrellaxd/mikan-proxy
```

## 配置

| 环境变量 | 默认值 | 说明 |
| -------- | ------ | ---- |
| URL |  | 你的域名 |
| PORT | 6789 | 服务端口 |

## 代理

推荐使用 NGINX 反代并配置证书。
可选用 `nginx-proxy-manager`。