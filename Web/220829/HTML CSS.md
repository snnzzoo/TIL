# 🦕 HTML

> HTML(**H**yper**t**ext **M**arkup **L**anguage)
>
> 프로그래밍 언어가 아닌, 컨텐츠의 구조를 정의하는 마크업 언어



## HTML의 요소

1. **여는 태그(opening tag)**: 요소의 이름으로 구성되고 여닫는 꺾쇠괄호로 감싸진다. 요소가 시작되는 곳, 또는 효과를 시작하는 곳임을 나타낸다.
2. **닫는 태그(closing tag)**: 여는 태그와 같지만, 요소의 이름 앞에 전방향 슬래시가 포함된다. 요소의 끝을 나타낸다 닫는 태그를 쓰지 않으면 결과가 표시된다.
3. **컨텐츠(content)**: 요소의 내용(content)
4. **요소(element)**: 요소는 여는 태그와 닫는 태그, 그리고 컨텐츠로 이루어진다. 중첩이 가능하다.



## HTML 문서 해부

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

- `<!DOCTYPE html>` 
  - HTML 초기에 (자동 오류 확인이나 다른 유용한 것을 의미하는) good HTML로 인정받기 위해 HTML 페이지가 따라야 할 일련의 규칙으로의 연결통로로써 작동하는 것을 의미하였다. 하지만 최근에는 그저 모든 것이 올바르게 동작하게 하기 위해 포함되어야 할 형식적인 것일 뿐이다.
- `<html></html>` 
  - `<html>`요소
  - 페이지 전체의 컨텐츠를 감싸며, 루트(root) 요소라고도 한다.
- `<head></head>`
  - `<head>`요소
  - HTML 페이지에 포함되어 있는 모든 것들(페이지를 조회하는 사람들에게 보여주지 않을 컨텐츠)의 컨테이너 역할
  - keywords와 검색 결과에 표시되길 원하는 페이지 설명, 컨텐츠를 꾸미기 위한 CSS, 문자 집합 선언 등과 같은 것들이 포함
- `<body></body>`
  - `<body>`요소
  - 페이지에 방문한 모든 웹 사용자들에게 보여주길 원하는 *모든* 컨텐트를 담고 있으며, 그것이 텍스트일 수도, 이미지, 비디오, 게임, 플레이할 수 있는 오디오 트랙이나 다른 무엇이든 될 수 있다.
- `<meta charset="utf-8">`
  - 문서가 사용해야 할 문자 집합을 utf-8으로 설정한다(utf-8 문자 집합에는 인간의 방대한 주류 기록언어에 있는 대부분의 문자가 포함되어 있다).
  - 본질적으로 사용할 수 있는 어떠한 문자 컨텐트도 다룰 수 있다. 이 문자 집합을 설정하지 않을 이유가 없으며, 그렇게 설정하면 나중에 발생할 수 있는 일부 문제를 피할 수 있다.
- `<title></title>` 
  - `<title>`요소. 이 요소는 페이지의 제목을 설정하는 것으로 페이지가 로드되는 브라우저의 탭에 이 제목이 표시된다. 이 요소는 북마크나 즐겨찾기에서 페이지를 설명하는 것으로도 사용된다.



🌴 [HTML의 메타데이터 정리]()




## 이미지

```html
<img src="images/firefox-icon.png" alt="My test image">
```



## 문자 나타내기

### 제목

```html
<h1>My main title</h1>
<h2>My top level heading</h2>
<h3>My subheading</h3>
<h4>My sub-subheading</h4>
<h5>My sub-sub-subheading</h5>
<h6>My sub-sub-sub-subheading</h6>
```



### 문단

```html
<p>This is a single paragraph</p>
```



### 목록

1. 순서가 없는 리스트

   ```html
   <p>At Mozilla, we’re a global community of</p>
   
   <ul>
     <li>technologists</li>
     <li>thinkers</li>
     <li>builders</li>
   </ul>
   
   <p>working together ... </p>
   ```

   

2. 순서가 있는 리스트

   ```html
   <p>At Mozilla, we’re a global community of</p>
   
   <ol>
     <li>technologists</li>
     <li>thinkers</li>
     <li>builders</li>
   </ol>
   
   <p>working together ... </p>
   
   ```

   

### 연결

`<a>`(anchor의 약자) 사용

```html
<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>
```





# 🦖 CSS

> CSS (**C**ascading **S**tyle **S**heets)
>
> 실제로 프로그래밍 언어도 *마크업(markup) 언어* 도 아닌, 웹페이지를 꾸미려고 작성하는 *Style sheet 언어* 



## CSS의 ruleset 해부

- 선택자(selector)

  - rule set의 맨 앞에 있는 HTML 요소 이름
  - 꾸밀 요소를 선택한다. 다른 요소를 꾸미기 위해서는 선택자만 바꾸면 된다.

- 선언

  - `color: red`와 같은 단일 규칙

  - 꾸미기 원하는 요소의 속성을 명시한다.

- 속성(property)

  - 주어진 HTML 요소를 꾸밀 수 있는 방법
  - CSS에서, rule 내에서 영향을 줄 속성을 선택한다.

- 속성 값

  - 속성의 오른쪽에, 콜론 뒤에, 주어진 속성을 위한 많은 가능한 결과중 하나를 선택하기 위해 속성 값을 갖는다. (`color` 의 값에는 `red` 외에 많은 것이 있습니다).

- 각각의 rule set (셀렉터로 구분) 은 반드시 (`{}`) 로 감싸져야 한다.

- 각각의 선언 안에, 각 속성을 해당 값과 구분하기 위해 콜론 (:)을 사용해야만 한다.

- 각각의 rule set 안에, 각 선언을 그 다음 선언으로부터 구분하기 위해 세미콜론 (;)을 사용해야만 한다.

```css
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

- 여러 요소도 선택 가능하다.

```css
p,li,h1 {
  color: red;
}
```

| 선택자 이름                                       | 선택하는 것                                                  | 예시                                                         |
| ------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 요소 선택자 (때때로 태그 또는 타입 선택자라 불림) | 특정 타입의 모든 HTML 요소                                   | `p` `<p> 를 선택`                                            |
| 아이디 선택자                                     | 특정 아이디를 가진 페이지의 요소 (주어진 HTML 페이지에서, 아이디당 딱 하나의 요소만 허용됩니다) | `#my-id` `<p id="my-id">` 또는 `<a id="my-id">` 를 선택      |
| 클래스 선택자                                     | 특정 클래스를 가진 페이지의 요소 (한 페이지에 클래스가 여러번 나타날 수 있습니다) | `.my-class` `<p class="my-class">` 와 `<a class="my-class">` 를 선택 |
| 속성 선택자                                       | 특정 속성을 갖는 페이지의 요소                               | `img[src]` `<img src="myimage.png">` 를 선택하지만 `<img> `는 선택 안함 |
| 수도(Pseudo) 클래스 선택자                        | 특정 요소이지만 특정 상태에 있을 때만, 예를 들면, hover over 상태일 때 | `a:hover` `<a>` 를 선택하지만, 마우스 포인터가 링크위에 있을 때만 선택함 |



## 글꼴과 문자





