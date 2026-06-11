-- ==========================================
-- SQL 入门篇（牛客网刷题记录）
-- 来源：牛客网 SQL 快速入门 全部题目
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


-- ============================================================
-- 题21：INNER JOIN 关联两张表
-- 题目：查看所有来自浙江大学的用户题目回答明细情况
-- 知识点：INNER JOIN ... ON + WHERE + ORDER BY
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
-- 题22：每个学校"答过题的用户"平均答题数量
-- 题目：运营想要了解每个学校答过题的用户平均答题数量情况
-- 知识点：COUNT / COUNT(DISTINCT) + GROUP BY（总答题数 ÷ 答题人数）
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
-- 题23：三表JOIN + 多字段分组
-- 题目：计算参加了答题的不同学校、不同难度的用户平均答题量
-- 知识点：三表INNER JOIN + COUNT(DISTINCT) + ROUND + 多字段GROUP BY
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
-- 题24：三表JOIN + WHERE + 多字段分组
-- 题目：查看参加了答题的山东大学用户在不同难度下的平均答题题目数
-- 知识点：同题23，加了WHERE LIKE过滤
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
-- 题25：UNION ALL 合并查询（不去重）
-- 题目：分别查看学校为山东大学或者性别为男性的用户，结果不去重
-- 知识点：UNION ALL（不去重）vs UNION（去重）
-- ============================================================
SELECT device_id, gender, age, gpa FROM user_profile WHERE university = '山东大学'
UNION ALL
SELECT device_id, gender, age, gpa FROM user_profile WHERE gender = 'male';


-- ============================================================
-- 题26：CASE WHEN 年龄段分组（2段 + NULL处理）
-- 题目：将用户划分为25岁以下和25岁及以上两个年龄段，age为null也记为25岁以下
-- 知识点：CASE WHEN ... IS NULL OR ...
-- ============================================================
SELECT
    CASE WHEN age < 25 OR age IS NULL THEN '25岁以下'
         WHEN age >= 25 THEN '25岁及以上'
    END AS age_cut,
    COUNT(*) AS number
FROM user_profile
GROUP BY age_cut;


-- ============================================================
-- 题27：CASE WHEN 多分支 + NULL单独处理
-- 题目：将用户划分为20岁以下、20-24岁、25岁及以上，年龄为空返回"其他"
-- 知识点：CASE WHEN 多条件 + IS NULL 放最后
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
-- 题28：DAY() 提取日期 + 按月过滤
-- 题目：计算出2021年8月每天用户练习题目的数量
-- 知识点：DAY(date) + LIKE '2021-08%' + GROUP BY date
-- ============================================================
SELECT
    DAY(date) AS day,
    COUNT(question_id) AS question_cnt
FROM question_practice_detail
WHERE date LIKE '2021-08%'
GROUP BY date;


-- ============================================================
-- 题29：次日留存率
-- 题目：查看用户在某天刷题后第二天还会再来刷题的留存率
-- 知识点：LEFT JOIN + DISTINCT + DATE_ADD + 关键：AND要写在ON里不能写WHERE
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
-- 题30：CASE WHEN + LIKE 从复合字段解析数据
-- 题目：统计每个性别的用户分别有多少参赛者（profile字段格式：device_id,gender,age,university）
-- 知识点：CASE WHEN LIKE 匹配字符串末尾
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
-- 题31：SUBSTRING_INDEX 提取URL最后一段
-- 题目：blog_url中提取用户个人博客用户名（URL最后一个/之后的部分）
-- 知识点：SUBSTRING_INDEX(str, '/', -1)  负数=从右往左取
-- ============================================================
SELECT
    device_id,
    SUBSTRING_INDEX(blog_url, '/', -1) AS user_name
FROM user_submit;


-- ============================================================
-- 题32：SUBSTRING_INDEX 嵌套提取中间字段
-- 题目：统计每个年龄的用户分别有多少参赛者（profile格式：device_id,gender,age,university）
-- 知识点：SUBSTRING_INDEX 嵌套——先切后两段，再取第一段
-- ============================================================
SELECT
    SUBSTRING_INDEX(SUBSTRING_INDEX(profile, ',', -2), ',', 1) AS age,
    COUNT(*) AS number
FROM user_submit
GROUP BY age;


-- ============================================================
-- 题33：多列子查询 找每组最小值对应的行
-- 题目：找到每个学校gpa最低的同学，取出device_id、university、gpa
-- 知识点：(col1, col2) IN (SELECT col1, MIN(col2) FROM ... GROUP BY col1)
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
-- 题34：LEFT JOIN + 条件写在ON里保留未匹配行
-- 题目：复旦大学每个用户8月份练习的总题目数和正确数，没练习过的返回0
-- 知识点：日期条件写在ON里（不是WHERE），LEFT JOIN保留没配上的行，SUM(CASE WHEN)
-- 关键：如果日期写成WHERE，没练习过的人会被整个删掉！
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
-- 题35：正确率计算 + 三表JOIN
-- 题目：浙江大学用户在不同难度题目下答题的正确率，按准确率升序
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
-- 题36：单字段排序
-- 题目：取出用户设备ID和年龄，按照年龄升序排序
-- 知识点：ORDER BY 单字段 ASC
-- ============================================================
SELECT device_id, age FROM user_profile ORDER BY age ASC;


-- ============================================================
-- 题37：多字段升序
-- 题目：取出device_id、gpa和age，先按gpa升序，再按年龄升序
-- 知识点：ORDER BY 多字段，优先级从左到右
-- ============================================================
SELECT device_id, gpa, age FROM user_profile ORDER BY gpa, age ASC;


-- ============================================================
-- 题38：多字段降序
-- 题目：先按照gpa降序、gpa相同的按照年龄降序排序
-- 知识点：ORDER BY 多字段 DESC
-- ============================================================
SELECT device_id, gpa, age FROM user_profile ORDER BY gpa DESC, age DESC;


-- ============================================================
-- 题39：COUNT DISTINCT + BETWEEN
-- 题目：2021年8月份所有练习过题目的总用户数和总次数
-- 知识点：COUNT(DISTINCT) + BETWEEN AND
-- ============================================================
SELECT
    COUNT(DISTINCT device_id) AS did_cnt,
    COUNT(question_id) AS question_cnt
FROM question_practice_detail
WHERE date BETWEEN '2021-08-01' AND '2021-08-31';


-- ============================================================
-- 题40：REGEXP 正则匹配
-- 题目：查询电话号码：10位数字、第一位非0、可用-分隔或连续
-- 知识点：REGEXP + 正则 '^[1-9][0-9]{2}-?[0-9]{3}-?[0-9]{4}$'
-- ============================================================
SELECT
    id,
    name,
    phone_number
FROM contacts
WHERE phone_number REGEXP '^[1-9][0-9]{2}-?[0-9]{3}-?[0-9]{4}$';


-- ============================================================
-- 题41：窗口函数 SUM() OVER
-- 题目：计算每一天的累计利润，按profit_date升序
-- 知识点：SUM(profit) OVER (ORDER BY profit_date)  窗口函数=累计求和
-- ============================================================
SELECT
    profit_id,
    profit_date,
    profit,
    SUM(profit) OVER (ORDER BY profit_date) AS cumulative_profit
FROM daily_profits;


-- ============================================================
-- 题42：数学函数 ABS / CEIL / FLOOR / ROUND
-- 题目：计算每个数值的绝对值、向上取整、向下取整、四舍五入到一位小数
-- 知识点：ABS() CEIL() FLOOR() ROUND(value, N)
-- ============================================================
SELECT
    *,
    ABS(value) AS absolute_value,
    CEIL(value) AS ceiling_value,
    FLOOR(value) AS floor_value,
    ROUND(value, 1) AS rounded_value
FROM numbers
ORDER BY id ASC;
