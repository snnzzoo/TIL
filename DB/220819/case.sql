-- 테이블 생성
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- 단순 조회
SELECT id, gender
FROM healthcare
LIMIT 5;
-- id  gender
-- --  ------
-- 1   1
-- 2   2
-- 3   2
-- 4   1
-- 5   2

-- 성별 1(남자), 2(여자)
SELECT
    id,
    CASE
        WHEN gender=1 THEN '남자'
        WHEN gender=2 THEN '여자'
        -- ELSE
    END AS 성별
FROM healthcare
LIMIT 5;

-- 흡연(smoking)
SELECT DISTINCT smoking
FROM healthcare;

SELECT
    id,
    smoking,
    CASE
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
        ELSE '무응답'
    END
FROM healthcare
LIMIT 50;


-- 테이블 생성
-- 정호,유,40,전라북도,016-7280-2855,370
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 데이터를 추가
.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로
.import users.csv users

-- 나이에 따라서 구분
-- 청소년(~18), 청년(~40), 중장년(~90)
SELECT 
    first_name,
    last_name,
    age,
    CASE 
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 35 THEN '청년'
        WHEN age <= 90 THEN '중장년'
        ELSE '노년' 
    END
FROM users
LIMIT 10;
