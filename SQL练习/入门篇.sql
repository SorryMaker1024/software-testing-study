-- ==========================================
-- SQL 入门篇（牛客网刷题记录）
-- 目标：20 题 | 正确率：17/20
-- ==========================================

-- 题1：查询所有数据 ✅
SELECT id, device_id, gender, age, university, province FROM user_profile;

-- 题2：查询指定列 ✅
SELECT device_id, gender, age, university FROM user_profile;

-- 题3：去重查询 ✅
SELECT DISTINCT university FROM user_profile;

-- 题4：限制行数 ✅
SELECT device_id FROM user_profile LIMIT 2;

-- 题5：重命名列 ✅
SELECT device_id AS user_infos_example FROM user_profile LIMIT 2;

-- 题6：条件过滤 ✅
SELECT device_id, university FROM user_profile WHERE university = '北京大学';

-- 题7：比较运算符 ✅
SELECT device_id, gender, age, university FROM user_profile WHERE age > 24;

-- 题8：范围查询 ✅
SELECT device_id, gender, age FROM user_profile WHERE age >= 20 AND age <= 23;

-- 题9：排除过滤 ✅
SELECT device_id, gender, age, university FROM user_profile WHERE university <> '复旦大学';

-- 题10：非空过滤 ✅
SELECT device_id, gender, age, university FROM user_profile WHERE age IS NOT NULL;

-- 题11：多条件AND ✅
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE gender = 'male' AND gpa > 3.5;

-- 题12：OR条件 ✅
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE university = '北京大学' OR gpa > 3.7;

-- 题13：多值匹配 ⚠️ 建议优化
-- 逻辑正确，但3个OR可改用IN更简洁：
-- WHERE university IN ('北京大学', '复旦大学', '山东大学')
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE university = '北京大学' OR university = '复旦大学' OR university = '山东大学';

-- 题14：复合条件+排序 ✅
SELECT device_id, gender, age, university, gpa FROM user_profile WHERE (gpa > 3.5 AND university = '山东大学') OR (gpa > 3.8 AND university = '复旦大学') ORDER BY device_id ASC;

-- 题15：模糊匹配 ✅
SELECT device_id, age, university FROM user_profile WHERE university LIKE '%北京%';

-- 题16：最高GPA ⚠️ 建议优化
-- 能跑通，但题目期望的写法是 SELECT MAX(gpa) FROM user_profile WHERE university = '复旦大学'
SELECT gpa FROM user_profile WHERE university = '复旦大学' ORDER BY gpa DESC LIMIT 1;

-- 题17：COUNT+AVG ✅
SELECT COUNT(gender) AS male_num, ROUND(AVG(gpa), 1) AS avg_gpa FROM user_profile WHERE gender = 'male';

-- 题18：多字段分组 ✅
SELECT gender, university, COUNT(*) AS user_num, ROUND(AVG(active_days_within_30), 1) AS avg_active_day, ROUND(AVG(question_cnt), 1) AS avg_question_cnt FROM user_profile GROUP BY gender, university ORDER BY gender, university;

-- 题19：HAVING ❌ 漏了ROUND(..., 3)
--！！！错误：题目要求结果保留3位小数，你的AVG没有用ROUND包裹，牛客网后台校验会不通过！！！
SELECT university, AVG(question_cnt) AS avg_question_cnt, AVG(answer_cnt) AS avg_answer_cnt FROM user_profile GROUP BY university HAVING avg_question_cnt < 5 OR avg_answer_cnt < 20;

-- 题20：分组+排序 ❌ 漏了ROUND(..., 4)
--！！！错误：题目要求结果保留4位小数，你的AVG没有用ROUND包裹，牛客网后台校验会不通过！！！
SELECT university, AVG(question_cnt) AS avg_question_cnt FROM user_profile GROUP BY university ORDER BY avg_question_cnt ASC;
