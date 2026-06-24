# Git 速成（测试岗够用）

> 你已经会了。这份文档是面试参考 + 常见场景速查。

---

## 一、核心流程（你已经每天在用了）

```
git add .              → 把改动加入暂存区
git commit -m "xxx"    → 提交到本地仓库
git push origin main   → 推到 GitHub
git pull origin main   → 拉取最新代码
```

---

## 二、面试必问：你工作中怎么用 Git？

> "我每天用 Git 管理测试代码。早上 git pull 拉最新代码，
> 写完用例后 git add → git commit → git push 提交。
> 如果测出新功能有 Bug，我会切一个新分支 git checkout -b bugfix/xxx，
> 在上面写好复现脚本，commit 后推到远程，关联到禅道的 Bug 单。"

---

## 三、常用命令速查

### 分支操作
```bash
git branch              # 查看所有本地分支
git branch bugfix/xxx   # 新建分支
git checkout bugfix/xxx # 切换到该分支
git checkout -b bugfix/xxx  # 新建 + 切换（一步到位）
git merge bugfix/xxx    # 把 bugfix 分支合并到当前分支
git branch -d bugfix/xxx    # 删除已合并的分支
```

### 查看历史
```bash
git log --oneline       # 一行一条，看最近提交
git log --oneline -10   # 只看最近10条
git status              # 看当前有哪些改动
git diff                 # 看改了什么内容
```

### 撤销操作
```bash
git checkout -- 文件名     # 撤销单个文件的修改（还没 add 的）
git reset HEAD 文件名       # 把 add 的文件撤回来
git reset --soft HEAD~1    # 撤销最近一次 commit，改动保留
git stash                   # 临时"藏"起当前改动
git stash pop               # 恢复刚才藏的改动
```

---

## 四、实战练习（现在做）

> 场景：模拟发现 Bug → 开分支 → 写复现脚本 → 提交 → 合并

```bash
# 1. 创建并切换到 bugfix 分支
git checkout -b bugfix/demo-login-bug

# 2. 新建一个"Bug复现说明.md"文件，随便写两句话

# 3. 提交
git add .
git commit -m "bugfix: 复现登录页密码为空时无提示的Bug"

# 4. 切回 main 合并
git checkout main
git merge bugfix/demo-login-bug

# 5. 删除 bugfix 分支
git branch -d bugfix/demo-login-bug

# 6. 推到远程
git push origin main
```

---

## 五、面试常见追问

| 问题 | 答案要点 |
|------|------|
| merge 和 rebase 的区别 | merge 保留分支历史，rebase 把提交"接"到主线末尾变线性。测试岗一般用 merge |
| git pull 和 git fetch 的区别 | fetch 只拉不合并，pull = fetch + merge。安全起见可以先 fetch 看看再 merge |
| 冲突怎么解决 | 多人改同一文件同一行时冲突。git 会标出 <<<<<< 和 >>>>>> ，手动选保留谁的代码，然后 add + commit |
| .gitignore 的作用 | 告诉 git 哪些文件不跟踪（如 node_modules、.pyc、IDE 配置） |

---

> 测试岗 Git 到此够用。重点是会用分支隔离 Bug 复现脚本，能和开发协作就行。
