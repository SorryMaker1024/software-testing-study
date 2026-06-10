-- ==========================================
-- SQL 入门篇（牛客网刷题记录）
-- 目标：20 题 | 正确率：17/20
-- ==========================================

-- ============================================================
-- 题1：查询所有数据 ✅
-- 题目：现在运营想要查看用户信息表中所有的数据，请你取出相应结果
-- 示例：user_profile (id, device_id, gender, age, university, province)
-- 返回：所有列
-- ============================================================
SELECT id, device_id, gender, age, university, province FROM user_profile;


-- ============================================================
-- 题2：查询指定列 ✅
-- 题目：运营同学想要用户的设备id对应的性别、年龄和学校的数据，请你取出相应数据
-- 返回：device_id, gender, age, university
-- ============================================================
SELECT device_id, gender, age, university FROM user_profile;


-- ============================================================
-- 题3：去重查询 ✅
-- 题目：运营需要查看用户来自于哪些学校，请从用户信息表中取出学校的去重数据
-- 返回：university
-- ============================================================
SELECT DISTINCT university FROM user_profile;


-- ============================================================
-- 题4：限制行数 ✅
-- 题目：运营只需要查看前2个用户明细设备ID数据，请你从用户信息表 user_profile 中取出相应结果
-- 返回：device_id
-- ============================================================
SELECT device_id FROM user_profile LIMIT 2;


-- ============================================================
-- 题5：重命名列 ✅
-- 题目：查看前2个用户明细设备ID数据，并将列名改为 'user_infos_example'
-- 返回：user_infos_example
-- ============================================================
SELECT device_id AS user_infos_example FROM user_profile LIMIT 2;


-- ============================================================
-- 题6：条件过滤 ✅
-- 题目：运营想要筛选出所有北京大学的学生进行用户调研，请你从用户信息表中取出满足条件的数据，结果返回设备id和学校
-- 返回：device_id, university
-- ============================================================
SELECT device_id, university FROM user_profile WHERE university = '北京大学';


-- ============================================================
-- 题7：比较运算符 ✅
-- 题目：运营想要针对24岁以上的用户开展分析，请你取出满足条件的设备ID、性别、年龄、学校
-- 返回：device_id, gender, age, university
-- ============================================================
SELECT device_id, gender, age, university FROM user_profile WHERE age > 24;


-- ============================================================
-- 题8：范围查询 ✅
-- 题目：运营想要针对20岁及以上且23岁及以下的用户开展分析，请你取出满足条件的设备ID、性别、年龄
-- 返回：device_id, gender, age
-- ============================================================
SELECT device_id, gender, age FROM user_profile WHERE age >= 20 AND age <= 23;


-- ============================================================
-- 题9：排除过滤 ✅
-- 题目：运营想要查看除复旦大学以外的所有用户明细包括的字段有 device_id、gender、age、university，请你取出相应数据
-- 返回：device_id, gender, age, university
-- ============================================================
SELECT device_id, gender, age, university FROM user_profile WHERE university <> '复旦大学';


-- ============================================================
-- 题10：非空过滤 ✅
-- 题目：运营想要对用户的年龄分布开展分析，在分析时想要剔除没有获取到年龄的用户，请你取出所有年龄值不为空的用户的设备ID，性别，年龄，学校的信息
-- 返回：device_id, gender, age, university
-- ============================================================
SELECT device_id, gender, age, university FROM user_profile WHERE age IS NOT NULL;


-- ============================================================
-- 题11：多条件AND ✅
-- 题目：运营想要找到male且GPA在3.5以上(不包括3.5)的用户进行调研，请你取出相关数据
-- 返回：device_id, gender, age, university, gpa
-- ============================================================
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE gender = 'male' AND gpa > 3.5;


-- ============================================================
-- 题12：OR条件 ✅
-- 题目：运营想要找到学校为北大或GPA在3.7以上(不包括3.7)的用户进行调研，请你取出相关数据（使用OR实现）
-- 返回：device_id, gender, age, university, gpa
-- ============================================================
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE university = '北京大学' OR gpa > 3.7;


-- ============================================================
-- 题13：多值匹配 ⚠️ 建议优化
-- 题目：运营想要找到学校为北大、复旦和山大的同学进行调研，请你取出相关数据
-- 返回：device_id, gender, age, university, gpa
-- 逻辑正确，但3个OR可改用 IN ('北京大学','复旦大学','山东大学') 更简洁
-- ============================================================
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE university = '北京大学' OR university = '复旦大学' OR university = '山东大学';


-- ============================================================
-- 题14：复合条件+排序 ✅
-- 题目：运营想要找到gpa在3.5以上(不包括3.5)的山东大学用户 或 gpa在3.8以上(不包括3.8)的复旦大学同学进行用户调研，请你取出相应数据,取出的数据按照device_id升序排列
-- 返回：device_id, gender, age, university, gpa
-- ============================================================
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE (gpa > 3.5 AND university = '山东大学') OR (gpa > 3.8 AND university = '复旦大学') ORDER BY device_id ASC;


-- ============================================================
-- 题15：模糊匹配 ✅
-- 题目：运营想查看所有大学中带有"北京"的用户的信息(device_id,age,university)，请你取出相应数据
-- 返回：device_id, age, university
-- ============================================================
SELECT device_id, age, university FROM user_profile WHERE university LIKE '%北京%';


-- ============================================================
-- 题16：最高GPA ⚠️ 建议优化
-- 题目：运营想要知道复旦大学学生gpa最高值是多少，请你取出相应数据，结果保留到小数点后面1位
-- 返回：gpa
-- 能跑通，但题目期望的写法是 SELECT MAX(gpa) FROM ... 更标准
-- ============================================================
SELECT gpa FROM user_profile WHERE university = '复旦大学' ORDER BY gpa DESC LIMIT 1;


-- ============================================================
-- 题17：COUNT+AVG ✅
-- 题目：运营想要看一下男性用户有多少人以及他们的平均gpa是多少，用以辅助设计相关活动，请你取出相应数据，结果使用round保留到小数点后面1位
-- 返回：male_num, avg_gpa
-- ============================================================
SELECT COUNT(gender) AS male_num, ROUND(AVG(gpa), 1) AS avg_gpa FROM user_profile WHERE gender = 'male';


-- ============================================================
-- 题18：多字段分组 ✅
-- 题目：运营想要对每个学校不同性别的用户活跃情况和发帖数量进行分析，请分别计算出每个学校每种性别的用户数、30天内平均活跃天数和平均发帖数量。结果保留1位小数，查询出来的结果按照gender、university升序排列
-- 返回：gender, university, user_num, avg_active_day, avg_question_cnt
-- ============================================================
SELECT gender, university, COUNT(*) AS user_num, ROUND(AVG(active_days_within_30), 1) AS avg_active_day, ROUND(AVG(question_cnt), 1) AS avg_question_cnt FROM user_profile GROUP BY gender, university ORDER BY gender, university;


-- ============================================================
-- 题19：HAVING ❌ 漏了ROUND(..., 3)
-- 题目：运营想查看每个学校用户的平均发贴和回帖情况，寻找低活跃度学校进行重点运营，请取出平均发贴数低于5的学校或平均回帖数小于20的学校。结果保留3位小数
-- 返回：university, avg_question_cnt, avg_answer_cnt
--！！！错误：漏了ROUND，牛客网后台校验会不通过！！！
-- ============================================================
SELECT university, AVG(question_cnt) AS avg_question_cnt, AVG(answer_cnt) AS avg_answer_cnt FROM user_profile GROUP BY university HAVING avg_question_cnt < 5 OR avg_answer_cnt < 20;


-- ============================================================
-- 题20：分组+排序 ❌ 漏了ROUND(..., 4)
-- 题目：运营想要查看不同大学的用户平均发帖情况，并期望结果按照平均发帖情况进行升序排列，请你取出相应数据
-- 返回：university, avg_question_cnt
--！！！错误：漏了ROUND，牛客网后台校验会不通过！！！
-- ============================================================
SELECT university, AVG(question_cnt) AS avg_question_cnt FROM user_profile GROUP BY university ORDER BY avg_question_cnt ASC;
