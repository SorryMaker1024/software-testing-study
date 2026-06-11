-- ==========================================
-- SQL 进阶篇（牛客网刷题记录）
-- 目标：30 题 | 已完成：20 题
-- ==========================================

-- ============================================================
-- 题1：浙江大学用户题目回答明细
-- 题目：运营想要查看所有来自浙江大学的用户题目回答明细情况
-- 知识点：INNER JOIN + WHERE + ORDER BY
-- ============================================================
SELECT
    question_practice_detail.device_id,
    question_practice_detail.question_id,
    question_practice_detail.result
FROM question_practice_detail
INNER JOIN user_profile
ON question_practice_detail.device_id = user_profile.device_id
WHERE university = '浙江大学'
ORDER BY question_id ASC;


-- ============================================================
-- 题2：每个学校答过题的用户平均答题数量
-- 题目：运营想要了解每个学校答过题的用户平均答题数量情况（总答题数 / 答题用户数）
-- 知识点：COUNT / COUNT(DISTINCT) + GROUP BY
-- ============================================================
SELECT
    user_profile.university,
    COUNT(question_practice_detail.question_id) / COUNT(DISTINCT question_practice_detail.device_id) AS avg_answer_cnt
FROM user_profile
INNER JOIN question_practice_detail
ON user_profile.device_id = question_practice_detail.device_id
GROUP BY user_profile.university
ORDER BY user_profile.university ASC;


-- ============================================================
-- 题3：不同学校+不同难度的用户平均答题量
-- 题目：计算一些参加了答题的不同学校、不同难度的用户平均答题量
-- 知识点：三表JOIN + COUNT(DISTINCT) + ROUND + 多字段GROUP BY
-- ============================================================
SELECT
    user_profile.university,
    question_detail.difficult_level,
    ROUND(COUNT(question_practice_detail.question_id) / COUNT(DISTINCT user_profile.device_id), 4) AS avg_answer_cnt
FROM user_profile
INNER JOIN question_practice_detail
ON user_profile.device_id = question_practice_detail.device_id
INNER JOIN question_detail
ON question_practice_detail.question_id = question_detail.question_id
GROUP BY user_profile.university, question_detail.difficult_level;


-- ============================================================
-- 题4：山东大学在不同难度下的平均答题题目数
-- 题目：查看参加了答题的山东大学的用户在不同难度下的平均答题题目数
-- 知识点：三表JOIN + WHERE LIKE + GROUP BY + ROUND
-- ============================================================
SELECT
    user_profile.university,
    question_detail.difficult_level,
    ROUND(COUNT(question_practice_detail.question_id) / COUNT(DISTINCT question_practice_detail.device_id), 4) AS avg_answer_cnt
FROM user_profile
INNER JOIN question_practice_detail
ON user_profile.device_id = question_practice_detail.device_id
INNER JOIN question_detail
ON question_practice_detail.question_id = question_detail.question_id
WHERE user_profile.university LIKE '%山东%'
GROUP BY user_profile.university, question_detail.difficult_level;


-- ============================================================
-- 题5：UNION ALL 合并查询
-- 题目：分别查看学校为山东大学或者性别为男性的用户的device_id、gender、age和gpa数据，结果不去重
-- 知识点：UNION ALL（不去重合并） vs UNION（去重合并）
-- ============================================================
SELECT device_id, gender, age, gpa FROM user_profile WHERE university = '山东大学'
UNION ALL
SELECT device_id, gender, age, gpa FROM user_profile WHERE gender = 'male';


-- ============================================================
-- 题6：CASE WHEN 年龄段分组（2段）
-- 题目：将用户划分为25岁以下和25岁及以上两个年龄段，分别查看用户数量（age为null也记为25岁以下）
-- 知识点：CASE WHEN + COUNT
-- ============================================================
SELECT
    CASE WHEN age < 25 OR age IS NULL THEN '25岁以下'
         WHEN age >= 25 THEN '25岁及以上'
    END AS age_cut,
    COUNT(*) AS number
FROM user_profile
GROUP BY age_cut;


-- ============================================================
-- 题7：CASE WHEN 年龄段分组（3段+空值处理）
-- 题目：将用户划分为20岁以下、20-24岁、25岁及以上三个年龄段，查看不同年龄段用户明细（年龄为空返回"其他"）
-- 知识点：CASE WHEN 多分支 + NULL 单独处理
-- ============================================================
SELECT
    device_id,
    gender,
    CASE WHEN age < 20 THEN '20岁以下'
         WHEN age >= 20 AND age <= 24 THEN '20-24岁'
         WHEN age >= 25 THEN '25岁及以上'
         WHEN age IS NULL THEN '其他'
    END AS age_cut
FROM user_profile;


-- ============================================================
-- 题8：2021年8月每天练习题目的数量
-- 题目：计算出2021年8月每天用户练习题目的数量
-- 知识点：DAY() 提取日 + LIKE 过滤月份 + GROUP BY
-- ============================================================
SELECT
    DAY(date) AS day,
    COUNT(question_id) AS question_cnt
FROM question_practice_detail
WHERE date LIKE '2021-08%'
GROUP BY date;


-- ============================================================
-- 题9：次日留存率
-- 题目：查看用户在某天刷题后第二天还会再来刷题的留存率
-- 知识点：LEFT JOIN + DISTINCT + DATE_ADD + 留存率公式
-- ============================================================
SELECT
    COUNT(q2.device_id) / COUNT(q1.device_id) AS avg_ret
FROM
    (SELECT DISTINCT device_id, date FROM question_practice_detail) AS q1
    LEFT JOIN
    (SELECT DISTINCT device_id, date FROM question_practice_detail) AS q2
    ON q1.device_id = q2.device_id
    AND q2.date = DATE_ADD(q1.date, INTERVAL 1 DAY);


-- ============================================================
-- 题10：从字符串字段解析性别
-- 题目：统计每个性别的用户分别有多少参赛者（profile字段格式：device_id,gender,age,university）
-- 知识点：CASE WHEN + LIKE 解析复合字段
-- ============================================================
SELECT
    CASE
        WHEN profile LIKE '%,male' THEN 'male'
        WHEN profile LIKE '%,female' THEN 'female'
    END AS gender,
    COUNT(device_id) AS number
FROM user_submit
GROUP BY gender;


-- ============================================================
-- 题11：SUBSTRING_INDEX 提取URL用户名
-- 题目：blog_url字段中url字符后的字符串为用户个人博客的用户名，提取出来
-- 知识点：SUBSTRING_INDEX(str, delimiter, count)，负数表示从右往左
-- ============================================================
SELECT
    device_id,
    SUBSTRING_INDEX(blog_url, '/', -1) AS user_name
FROM user_submit;


-- ============================================================
-- 题12：嵌套SUBSTRING_INDEX 提取年龄
-- 题目：统计每个年龄的用户分别有多少参赛者（profile字段格式：device_id,gender,age,university）
-- 知识点：SUBSTRING_INDEX 嵌套使用提取中间字段
-- ============================================================
SELECT
    SUBSTRING_INDEX(SUBSTRING_INDEX(profile, ',', -2), ',', 1) AS age,
    COUNT(*) AS number
FROM user_submit
GROUP BY age;


-- ============================================================
-- 题13：多列子查询找每组最低GPA
-- 题目：找到每个学校gpa最低的同学来做调研，取出device_id、university、gpa
-- 知识点：(col1, col2) IN (SELECT col1, col2 FROM ...) 多列子查询
-- ============================================================
SELECT
    device_id,
    university,
    gpa
FROM user_profile
WHERE (university, gpa) IN (
    SELECT university, MIN(gpa)
    FROM user_profile
    GROUP BY university
)
ORDER BY university;


-- ============================================================
-- 题14：复旦大学8月份练习情况（含未练习用户）
-- 题目：了解复旦大学的每个用户在8月份练习的总题目数和回答正确的题目数，8月没有练习过的答题数返回0
-- 知识点：LEFT JOIN + ON里放日期条件 + SUM(CASE WHEN)
-- 关键：日期条件写在ON里而不是WHERE，保证LEFT JOIN保留没配上的行
-- ============================================================
SELECT
    up.device_id,
    up.university,
    COUNT(qpd.question_id) AS question_cnt,
    SUM(CASE WHEN qpd.result = 'right' THEN 1 ELSE 0 END) AS right_question_cnt
FROM user_profile up
LEFT JOIN question_practice_detail qpd
    ON up.device_id = qpd.device_id
    AND qpd.date BETWEEN '2021-08-01' AND DATE_ADD('2021-08-01', INTERVAL 30 DAY)
WHERE up.university = '复旦大学'
GROUP BY up.device_id, up.university
ORDER BY up.device_id ASC;


-- ============================================================
-- 题15：浙江大学不同难度题目正确率
-- 题目：了解浙江大学的用户在不同难度题目下答题的正确率，按准确率升序
-- 知识点：SUM(CASE WHEN) / COUNT + ROUND + 三表JOIN
-- ============================================================
SELECT
    qd.difficult_level,
    ROUND(SUM(CASE WHEN qpd.result = 'right' THEN 1 ELSE 0 END) / COUNT(qpd.question_id), 4) AS correct_rate
FROM user_profile up
INNER JOIN question_practice_detail qpd
    ON up.device_id = qpd.device_id
INNER JOIN question_detail qd
    ON qpd.question_id = qd.question_id
WHERE up.university = '浙江大学'
GROUP BY qd.difficult_level
ORDER BY correct_rate ASC;


-- ============================================================
-- 题16：单字段升序排序
-- 题目：取出用户设备ID和年龄，按照年龄升序排序
-- 知识点：ORDER BY 单字段 ASC
-- ============================================================
SELECT
    device_id,
    age
FROM user_profile
ORDER BY age ASC;


-- ============================================================
-- 题17：多字段升序排序
-- 题目：取出device_id、gpa和age，先按照gpa升序，再按照年龄升序
-- 知识点：ORDER BY 多字段，优先级从左到右
-- ============================================================
SELECT
    device_id,
    gpa,
    age
FROM user_profile
ORDER BY gpa, age ASC;


-- ============================================================
-- 题18：多字段降序排序
-- 题目：先按照gpa降序、gpa相同的按照年龄降序排序
-- 知识点：ORDER BY 多字段 DESC
-- ============================================================
SELECT
    device_id,
    gpa,
    age
FROM user_profile
ORDER BY gpa DESC, age DESC;


-- ============================================================
-- 题19：COUNT DISTINCT + BETWEEN
-- 题目：了解2021年8月份所有练习过题目的总用户数和练习过题目的总次数
-- 知识点：COUNT(DISTINCT) + BETWEEN AND
-- ============================================================
SELECT
    COUNT(DISTINCT device_id) AS did_cnt,
    COUNT(question_id) AS question_cnt
FROM question_practice_detail
WHERE date BETWEEN '2021-08-01' AND '2021-08-31';


-- ============================================================
-- 题20：REGEXP 正则匹配电话号码
-- 题目：查询符合以下条件的电话号码：10位数字、第一位不能以0开头、格式可以是连续的10位数字或以-分隔
-- 知识点：REGEXP + 正则表达式 '^[1-9][0-9]{2}-?[0-9]{3}-?[0-9]{4}$'
-- ============================================================
SELECT
    id,
    name,
    phone_number
FROM contacts
WHERE phone_number REGEXP '^[1-9][0-9]{2}-?[0-9]{3}-?[0-9]{4}$';


-- ============================================================
-- 题21：累计利润（窗口函数）
-- 题目：计算每一种产品每一天的累计利润，按profit_date升序
-- 知识点：SUM() OVER (PARTITION BY ... ORDER BY ...) 窗口函数
-- ============================================================
-- 我的答案：
