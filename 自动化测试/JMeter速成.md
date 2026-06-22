# JMeter 性能测试速成（了解即可）

> JMeter 是 Apache 开源的性能测试工具，纯 Java 开发。
> 能模拟多用户并发请求，看系统的吞吐量、响应时间。

---

## 一、JMeter 能干什么

| 场景 | 说明 |
|------|------|
| 接口性能测试 | 100 个人同时访问一个接口，系统撑得住吗？ |
| 压力测试 | 不断加人直到系统崩，找瓶颈 |
| 稳定性测试 | 持续跑 1 小时，看内存泄漏、CPU 变化 |

---

## 二、核心概念（3 层结构）

```
Test Plan（测试计划，最外层）
  └── Thread Group（线程组 = 虚拟用户）
        └── HTTP Request（发什么请求）
        └── Listener（看结果：聚合报告、图表）
```

| 概念 | 类比 |
|------|------|
| Thread Group | 多少个"人"并发访问 |
| HTTP Request | 每个人做什么操作（GET/POST） |
| Listener | 最终看什么报告 |

---

## 三、关键指标（面试必问）

打开 JMeter 跑完一个请求后，点 **聚合报告（Aggregate Report）** 看这几个数：

| 指标 | 含义 | 好还是坏 |
|------|------|------|
| Samples | 发了多少次请求 | — |
| Average | 平均响应时间（ms） | < 500ms 好，> 2s 差 |
| Median | 50% 用户的响应时间 | 同上 |
| 90% Line | 90% 用户的响应时间 | 和 Average 差距大说明不稳定 |
| Error % | 错误率 | 必须 = 0% |
| Throughput | 吞吐量（请求/秒） | 越大越好 |
| Received KB/sec | 网络流量 | — |

---

## 四、动手操作（现在做）

### 启动 JMeter

```
双击 E:\apache-jmeter-5.6.3\bin\jmeter.bat
或终端运行：
E:\apache-jmeter-5.6.3\bin\jmeter.bat
```

### 步骤

1. **Test Plan 右键 → Add → Threads → Thread Group**
   - Number of Threads: `10`（模拟 10 个用户）
   - Loop Count: `5`（每人重复 5 次 = 总共 50 次请求）

2. **Thread Group 右键 → Add → Sampler → HTTP Request**
   - Protocol: `https`
   - Server Name: `jsonplaceholder.typicode.com`
   - Method: `GET`
   - Path: `/posts/1`

3. **Thread Group 右键 → Add → Listener → View Results Tree**（看单次结果）
4. **Thread Group 右键 → Add → Listener → Aggregate Report**（看汇总报告）

5. **点工具栏绿色 ▶ 按钮** → 保存测试计划 → 跑！

### 看结果

切到 **Aggregate Report**，看 Average（平均响应时间）和 Throughput（吞吐量）。

---

## 五、面试怎么说

> "我用过 JMeter 做接口性能测试。创建一个 Thread Group 设置并发用户数，
> 添加 HTTP Request 配置要测的接口，加一个 Aggregate Report 监听器看结果。
> 关注的核心指标是平均响应时间、错误率、吞吐量。如果响应时间超过预期
> 或者出现错误，就去查是数据库慢还是接口逻辑有问题。"

---

## 六、跟 Postman 的区别

| | Postman | JMeter |
|------|------|------|
| 用途 | 单次调试、自动化测试 | 性能压测、负载测试 |
| 并发 | Collection Runner 顺序跑 | 真正多线程并发 |
| 报告 | 简单 Pass/Fail | 详细的响应时间、吞吐量图表 |
