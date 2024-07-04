### 사용 이유
생성자 방식은 필드 값을 세팅할 때 순서가 정해져 있고, 매개변수도 지정해주어야함.
객체가 가지고 있는 인자가 많을 경우 생성자 사용에서 헷갈려 실수가 발생할 수 있음.

### Builder 패턴이란?
빌더 패턴(Builder pattern)이란 복합 객체의 생성 과정과 표현 방법을 분리하여 동일한 생성 절차에서 서로 다른 표현 결과를 만들 수 있게 하는 패턴.

```
public class Member {
	private Long id;
	private String name;
	private String address;

	public Member(Long id, String name, String address) {
	this.id = id;
	this.name = name;
	this.address = address;
	}
}
```

만약 필드 값의 종류가 많아진다면,
```
Member member = new Member(1L, "yeonjae", "seoul", "...", "...", .....)
```
생성자 방식은 필드 값 생성 시에 순서가 정해져 있기 때문에 필드 값의 종류가 많으면 헷갈릴 수 있다.

## 해결법

### 1. setter 사용 (비추)

```
public class Member {
	private Long id;
	private String name;
	private String address;

	public void setId(Long id) {
		this.id=id;
	}
	public void setName(Long id) {
		this.name=name;
	}
	public void setAddress(Long id) {
		this.address=address;
	}
}
```
<필드 값 세팅>
```
Member member = new Member();
member.setId(1L);
member.setName("yeonjae");
member.setAddress("seoul");
```
setName과 같이 어떤 필드를 세팅하는지 쉽게 알 수 있게 되었으나 setter를 사용하게 되면 필드 값에 대한 불변성이 보장되지 않기 때문에 사용을 자제하는 것이 좋다.

## 2. 빌더 패턴 사용
```
    public class Member {  
    private Long id;  
    private String name;  
    private String address;  
  
    public Member(Builder builder) {  
    //생성자. Member로 변환하는 build 메소드에서 사용
        this.id=builder.id;  
        this.name=builder.name;  
        this.address=builder.address;  
    }  
    public static Builder builder() {  
    //외부에서 Builder를 생성
        return new Builder();  
    }  
  
    public static class Builder {  
        private Long id;  
        private String name;  
        private String address;  
  
        public Builder id(Long id) {  
            this.id = id;  
            return this;  
        }        public Builder name(String name) {  
            this.name = name;  
            return this;  
        }        public Builder address(String address) {  
            this.address = address;  
            return this;  
        }  
        public Member build() {  
        //Member로 변환
            return new Member(this);  
        }    }  
}
```

```
Member member = Member.builder()  
        .id(1L)  
        .name("yeonjae")  
        .address("seoul")  
        .build();
```
이렇게 사용!

1.
```
public class Member {  
    private Long id;  
    private String name;  
    private String address;  
  
    public Member(Builder builder) {  
        this.id=builder.id;  
        this.name=builder.name;  
        this.address=builder.address;  
    }
```
Member 클래스 내부 static class에는 Builder 클래스가 들어있다.
이 Builder 클래스는 Member 클래스의 필드 값을 가지고 있다.

2.
```
public static class Builder {  
    private Long id;  
    private String name;  
    private String address;  
  
    public Builder id(Long id) {  
        this.id = id;  
        return this;  
    }    public Builder name(String name) {  
        this.name = name;  
        return this;  
    }    public Builder address(String address) {  
        this.address = address;  
        return this;  
    }  
    public Member build() {  
        return new Member(this);  
    }}
```
빌더의 메소드를 정의한다. 이 메소드들은 Builder의 필드 값을 세팅하고 Builder를 반환하는 메소드이다.
원하는 메소드를 호출하고 나면 그에 해당하는 필드 값들이 Builder에 세팅되어 있으므로 해당 Builder를 Member로 변환한다. 이를 위해 Member의 생성자 및 build 메소드를 구현한다.

## Assert 적절히 적용하자
hasText, notNull 등의 메소드 존재