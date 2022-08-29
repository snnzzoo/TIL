# 🐱‍🏍 HTML의 메타데이터

## 🐱‍💻 HTML head

- HTML `<head>`요소의 내용

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```

페이지를 열 때 브라우저에 표시되는 `<body>`요소와 다르게, head의 내용는 페이지에 표시되지 않는다. 대신에 head의 내용이 하는 일은 페이지에 대한 [metadata](https://developer.mozilla.org/ko/docs/Glossary/Metadata)를 포함하는 것이다.



## 🐱‍💻 제목 달기

- `<h1>`
  - 일반적으로 페이지당 한 번 씩 사용되는데, 페이지 내용물의 제목이나 뉴스의 헤드라인을 표시하기 위해서 페이지를 열 때 브라우저에 표시된다.
- `<title>`
  - (문서의 컨텐츠가 아니라) HTML문서 전체의 타이틀 표현하기 위한 메타데이터이다.



## 🐱‍💻 메타데이터 : `<meta>` 요소

메타데이터는 데이터를 설명하는 데이터이다.



### 문서의 character 인코딩 특정하기

```html
<meta charset="utf-8">
```

- 문서의 character—문서에서 허용하는 문자 집합(character set)— encoding에 대해서 간단히 표시한다 .
- `utf-8` 은 전세계적인 character 집합으로 많은 언어들을 문자들을 포함한다. 이는 웹 페이지에서 어떤 문자라도 취급할 수 있다는 것을 의미합니다.



### 저자와 설명을 추가

```html
<meta name="author" content="Chris Mills">
<meta name="description" content="The MDN Learning Area aims to provide
complete beginners to the Web with all they need to know to get
started with developing web sites and applications.">
```

많은 `<meta>` 요소가 `name` 과 `content` 속성을 가진다:

- `name` 은 메타 요소가 어떤 정보의 형태를 갖고 있는지 알려준다.
- `content`는 실제 메타데이터의 컨텐츠이다.

이러한 두가지 메타데이터는 당신의 페이지에서 관리자를 정리하고 머릿말을 요약하는데 유용하다.



저자를 지정하는 것은 콘텐츠 작성자에 대한 정보를 볼 수 있게 해준다. 일부 컨텐츠 관리 시스템에는 페이지 작성자 정보를 자동으로 추출해서 사용할 수 있는 기능이 있다.

페이지 콘텐츠 관련 키워드를 포함시키는 것은 검색엔진에서 이 페이지가 더 많이 표시 될 가능성이 생기게 할 수 있다. (이러한 활동을 [Search Engine Optimization](https://developer.mozilla.org/ko/docs/Glossary/SEO), 또는 [SEO](https://developer.mozilla.org/ko/docs/Glossary/SEO) 라고 함.)



### Other types fo metadata

웹페이지를 돌아다니다 보면 다른 종류의 메타데이터들을 꽤 많이 볼 수 있다. 웹 사이트에서 볼 수있는 기능들은 특정 사이트 (예 : 소셜 네트워킹 사이트)에 사용할 수있는 특정 정보를 제공하도록 설계된 독점 제작물이다.

- Open Graph Data

  - 웹페이지를 돌아다니다 보면 다른 종류의 메타데이터들을 꽤 많이 볼 수 있다. 웹 사이트에서 볼 수있는 기능들은 특정 사이트 (예 : 소셜 네트워킹 사이트)에 사용할 수있는 특정 정보를 제공하도록 설계된 독점 제작물

  ```html
  <meta property="og:image" content="https://developer.mozilla.org/static/img/opengraph-logo.png">
  <meta property="og:description" content="The Mozilla Developer Network (MDN) provides
  information about Open Web technologies including HTML, CSS, and APIs for both Web sites
  and HTML5 Apps. It also documents Mozilla products, like Firefox OS.">
  <meta property="og:title" content="Mozilla Developer Network">
  ```

  - Facebook에서 MDN에 링크를 하면, 이미지와 설명이 함께 나타난다. 사용자에게는 더 좋은 정보를 보여줄 수 있게 된다.

- Twitter 에서도 유사한 형태의 독점적인 자체 메타데이터를 가지고 있는데, 특정 웹사이트의 url이 twitter.com에 표시 될 때와 유사한 효과가 있다.

  ```html
  <meta name="twitter:title" content="Mozilla Developer Network">
  ```



## 🐱‍💻 맞춤 아이콘 추가하기

사이트 디자인을 좀 더 풍성하게 만들기 위해서 , 커스텀 아이콘 레퍼런스를 매타데이터에 추가하고 특정 콘텐츠에서 이것을 보여지게 할 수 있다.

- favicon

  - 인터넷 웹 브라우저의 주소창에 표시되는 웹사이트나 웹페이지를 대표하는 아이콘이다.

  ![image-20220830015452628](220829 HTML 메타데이터.assets/image-20220830015452628.png)

  

  ```html
  <!-- third-generation iPad with high-resolution Retina display: -->
  <link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://developer.mozilla.org/static/img/favicon144.png">
  <!-- iPhone with high-resolution Retina display: -->
  <link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://developer.mozilla.org/static/img/favicon114.png">
  <!-- first- and second-generation iPad: -->
  <link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://developer.mozilla.org/static/img/favicon72.png">
  <!-- non-Retina iPhone, iPod Touch, and Android 2.1+ devices: -->
  <link rel="apple-touch-icon-precomposed" href="https://developer.mozilla.org/static/img/favicon57.png">
  <!-- basic favicon -->
  <link rel="shortcut icon" href="https://developer.mozilla.org/static/img/favicon32.png">
  ```

  주석은 각 아이콘의 용도를 설명한다. 웹사이트가 iPad의 홈 화면에 저장 될 때 사용할 고해상도 아이콘을 제공하는 것 등을 포함한다.



## 🐱‍💻 HTML에 CSS와 JavaScript 적용하기

현대의 모든 웹사이트는 상호작용 기능이 많은 영상 플레이어, 지도, 게임 등을 위해 [JavaScript](https://developer.mozilla.org/ko/docs/Glossary/JavaScript)가 필요하고, 이것들을 더 멋져 보이게 하기 위해 [CSS](https://developer.mozilla.org/ko/docs/Glossary/CSS)가 사용된다. 이것들은 `<link>`요소와 `<script>`요소를 사용하여 웹 페이지에 가장 일반적으로 적용된다.

- `<head>`

  - 항상 문서의 head 부분에 위치한다.
  - 이것은 두 가지 속성을 취하는데, `rel="stylesheet"`, 즉 문서의 스타일 시트임을 나타냄과 동시에 스타일 시트 파일의 경로를 포함하는 `href`를 내포한다.

  ```html
  <link rel="stylesheet" href="my-css-file.css">
  ```

- `<script>`

  -  head에 들어갈 필요가 없다. `</body>` 태그 바로 앞, 문서 본문의 맨 끝에 넣는 것이 좋으며, JavaScript를 적용하기 전에 모든 HTML 내용을 브라우저에서 읽었는지 확인하는 것이 좋다. 액세스 과정에서 JavaScript가 아직 존재하지 않는 요소라고 판단하며 에러가 날 수 있다.

  ```html
  <script src="my-js-file.js"></script>
  ```

  - ✏**Note**: `<script>` 태그가 비어있다고 보일 수 도 있지만 그렇지 않으며, 반드시 태그를 닫아주어야 한다(</script>). 외부 스크립트 파일을 지정하는 대신 스크립트를 `<script>` 안에 넣을 수 도 있다.



## 🐱‍💻 문서의 기본 언어 설정

마지막으로, 페이지의 언어를 설정 할 수도 있다. 이 작업은 [lang attribute](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/lang) 을 여는 HTML 태그에 추가하여 수행 할 수 있다.

```html
<html lang="en-US">
```

- HTML 문서는 언어가 설정되어 있으면 검색 엔진에 의해 보다 효과적으로 색인화된다.

  - 예시 : 언어 별 결과에 올바르게 표시된다.

- 화면 판독기를 사용하여 시각장애가 있는 사용자에게 유용하다.

- 또한, 문서의 하위 섹션을 다른 언어로 인식하도록 설정할 수도 있다. 예를들어 다음과 같이 일본어 일본어로 된 섹션에 대해서는 일본어로 인식하도록 할 수 있다:

  ```html
  <p>Japanese example: <span lang="jp">ご飯が熱い。</span>.</p>
  ```

