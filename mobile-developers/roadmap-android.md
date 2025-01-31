# Рекомендации от Контура для Android-разработчиков

Ниже представлен roadmap от Android-разработчиков Контура. Этот roadmap не претендует на абсолютную правду и является субъективным мнением авторов. По такому пути мы шли сами и хотели бы видеть таких коллег рядом.

## Roadmaps

Здесь представлены популярные маршруты знаний от разных авторов. Их цель – дать представление об Android-разработке и помочь сориентироваться в умениях и навыках.

- [Android Developer Roadmap for beginners](https://roadmap.sh/android)
- [Android Developer Roadmap 2](https://github.com/mobile-roadmap/android-developer-roadmap)
- [Android Developer Roadmap 3](https://trello.com/b/fsc44tYh/android-developer-roadmap)
- [Android Developer Roadmap 4](https://github.com/MindorksOpenSource/android-developer-roadmap)

## Level 1️: Intern

Стажер должен обладать знаниями, чтобы пройти порог входа в профессию программиста и в промышленную разработку. Эти материалы помогут попасть на твою первую стажировку в компанию, пройти испытательный срок и получить опыт в Android-разработке.

### Kotlin

<details>
  <summary>Почему Kotlin, а не Java?</summary>

В 2021 году уже нет большого смысла учить Java как первый язык программирования (ЯП).
Если сравнить ЯП с ездой на машине, то Java – это отечественный УАЗ на механике. Проедет везде, но удовольствия мало. Kotlin – иномарка на автомате. Идеальный вариант, чтобы учиться и ездить с комфортом в большом городе. Но это не значит, что не нужно учить JVM (Java Virtual Machine)
  
</details>

- Объявление переменных, типы данных. Понимать разницу между `val` и `var`.
- Логические выражения: `if/else`, `when`, `while`, `for`
- Базовые коллекции: `ArrayList`, `LinkedList`,`HashMap`, `LinkedHashMap`,`HashSet`, `ArrayDeque`
- [Модификаторы доступа](https://kotlinlang.ru/docs/reference/visibility-modifiers.html). Определяют откуда функция будет доступна для вызова. Например, некоторые функции можно скрыть для всех классов кроме того, в котором она объявлена. Это помогает в соблюдении принципа инкапсуляции.

<details>
  <summary>Функции, классы, интерфейсы и объекты</summary>
  
- Классы: обычные, data, sealed и enum.
- Интерфейсы
- Объекты

</details>

#### Источники

- Официальная документация [RUS](https://kotlinlang.ru) | [ENG](https://kotlinlang.org)
- [Playground](https://play.kotlinlang.org/), чтобы попробовать Kotlin
- [CodeWars](https://www.codewars.com) или [CodinGames](https://www.codingame.com/home), чтобы порешать задачки и держать себя в форме

### Android

- [Activity](https://developer.android.com/guide/components/activities/intro-activities) и [Fragments](https://www.raywenderlich.com/1364094-android-fragments-tutorial-an-introduction-with-kotlin).  
Это специальные классы, которые позволяют управлять экранами приложения. Активити – это один из базовых компонентов android-приложения, который предоставляет экран, с которым пользователи могут взаимодействовать, чтобы что-то делать. Фрагмент представляет поведение или часть пользовательского интерфейса в Активити.

- [The Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle) и [Fragment lifecycle](https://developer.android.com/guide/fragments/lifecycle).  
У приложения в целом, и у каждого экрана в отдельности есть свой жизненный цикл. С его помощью разработчики могут управлять поведением приложения, когда пользователь его открывает, закрывает, или переворачивает телефон

- [Xml разметка](https://www.youtube.com/watch?v=pjsADVZh45I).  
Файл, описывающий внешний вид экрана

- [Context](https://developer.alexanderklimov.ru/android/theory/context.php).  
C помощью этого класса можно взаимодействовать с системой Android

- [SharedPreferences](http://developer.alexanderklimov.ru/android/theory/sharedpreferences.php).  
Самый простой способ постоянно хранить данные в памяти. Данные хранятся по принципу «ключ - значение»

- [AndroidManifest.xml](http://developer.alexanderklimov.ru/android/theory/AndroidManifestXML.php).  
Файл, в котором указываются название приложения, его иконка, версия, разрешения, стартовая Activity и другие базовый компоненты приложения.

- [Gradle](https://riptutorial.com/android-gradle).  
Это система сборки проекта. В файлах gradle можно указать минимально поддерживаемую версию Android, подключить сторонние библиотеки, настроить правила, по которым будет собираться проект

- [RecyclerView](http://developer.alexanderklimov.ru/android/views/recyclerview-kot.php).  
Компонент для оптимизированной работы со списками данных

- [Паттерн MVVM](https://www.section.io/engineering-education/implementing-mvvm-architecture-in-android-using-kotlin/).  
Один из самых популярных презентационных паттернов в Android, который позволяет отделить бизнес логику от пользовательского интерфейса.

<details>
  <summary>Работа с сетью</summary>
  
- [JSON](https://ru.wikipedia.org/wiki/JSON) – текстовый формат обмена данными, в основном используется для обмена данными между клиентом и сервером

- Библиотека [Retrofit](https://github.com/square/retrofit)
Помогает создать интерфейс для работы с API.
Потренироваться в ее использовании можно на бесплатных API, например, [здесь](https://jsonplaceholder.typicode.com/todos)
  
</details>
<details>
  <summary>Базы данных</summary>
  
- Знать [принципы работы реляционных баз данных](https://www.oracle.com/ru/database/what-is-a-relational-database/)

- Библиотека [Room](https://developer.android.com/training/data-storage/room).  
Самая распространенная библиотека базы данных на Android. В ней есть методы для самых распространенных запросов. Если нужного метода нет - запрос придется писать самому. Для этого нужно знать как [составлять запросы на языке SQL](http://developer.alexanderklimov.ru/android/sqlite/android-sqlite.php)
  
</details>

#### Источники

- [Официальная документация](https://developer.android.com/docs)
- Канал [Start Android](https://www.youtube.com/channel/UCzE7HcbvyEiS5ea1rVRbPLQ), курс [Kotlin. Уроки по основам разработки android-приложений](https://www.youtube.com/watch?v=1ruPswojG6E&list=PLyfVjOYzujuj20Y-3kVhT3Zro9CrMNgNS)

<details>
  <summary>Курсы на Pluralsight</summary>
  
- [Курс Android Fundamentals](https://app.pluralsight.com/profile/author/sriyank-siddhartha)
- [Android Apps with Kotlin: Build Your First App](https://app.pluralsight.com/library/courses/android-apps-kotlin-build-first-app/table-of-contents)
- [Android Data Binding: Getting Started](https://app.pluralsight.com/library/courses/android-data-binding-getting-started/table-of-contents)
- [Android Apps with Kotlin: ViewModel and Lifecycle](https://app.pluralsight.com/library/courses/android-apps-kotlin-viewmodel-lifecycle/table-of-contents)
- [Android Fundamentals: Implementing Effective Navigation](https://app.pluralsight.com/library/courses/android-fundamentals-effective-navigation/table-of-contents)
- [Android Apps with Kotlin: Tools and Testing](https://app.pluralsight.com/library/courses/android-apps-kotlin-tools-testing/table-of-contents)
- [Android: Room Fundamentals](https://app.pluralsight.com/library/courses/android-room-fundamentals/table-of-contents)
- [Android: Getting Started with Retrofit](https://app.pluralsight.com/library/courses/android-retrofit-getting-started/table-of-contents)
  
</details>

### Git

Git – это одна из популярных систем контроля версий.

<details>
  <summary>Нужно уметь в базовые команды</summary>
  
- `git init`
- `git clone`
- `git remote add`
- `git add`
- `git commit`
- `git reset`
- `git branch`
- `git checkout`
- `git merge`
- `git rebase`
- `git push`
- `git fetch`
- `git pull`
  
</details>

#### Источники

- [Документация](https://git-scm.com/book/ru/v2)
- [Онлайн-тренажер 1](https://learngitbranching.js.org/)
- [Онлайн-тренажер 2](https://githowto.com/ru/)

### Принципы ООП

Принципы объектно-ориентированного программирования (ООП) помогают разделить код, дробя его на сущности, объединенные общей функциональностью.

Если следовать этим принципам, повторяющегося кода будет меньше, добавлять новые функции станет проще.

#### Источники

- [Принципы объектно-ориентированного программирования](https://javarush.ru/groups/posts/1966-principih-obhhektno-orientirovannogo-programmirovanija)
- [DRY](https://ru.wikipedia.org/wiki/Don’t_repeat_yourself)
- [KISS](https://ru.wikipedia.org/wiki/KISS_(принцип))

## Level 2️: `Junior`

Junior-разработчик – полноценный член команды разработки. Он пишет понятный, читаемый код. Хорошо знает язык, легко использует его стандартные методы и конструкции. Может самостоятельно проектировать задачи средней сложности.

### Kotlin

<details>
  <summary>Функции</summary>
  
- `extension fun`, `infix fun`, `inline fun`, `operator fun`
- `Generics`
  
</details>
<details>
  <summary>Синтаксический сахар</summary>
  
Так называют приятные мелочи языка, которые позволяют писать более простой и красивый код:

- Функции для работы с коллекциями: `forEach`, `map`, `flatMap`, `filter`, `sort`, `reduce`, `groupBy`, `orEmpty`, `getOrElse`
- Именованные аргументы
- `Single abstract method`
- Высокоуровневые функции и лямбды
- `Destructive declaration`
- `Labels`
- `let`, `apply`, `also`, `with`
  
</details>

### Android

<details>
  <summary>Разделение зон ответственности между разными компонентами приложения</summary>
  
- Изучил архитектурные паттерны MVP, MVVM, MVI
  
</details>

<details>
  <summary>Паттерны проектирования</summary>
  
- Factory
- Singleton
- Decorator
- Facade
- Command
- State
- Srategy
- Observer

Источники: [раз,](https://ru.wikipedia.org/wiki/Design_Patterns) [два](https://refactoring.guru/design-patterns/catalog)

</details>

- Работа с сетью
  - Иметь представление в каком виде приходят данные с сервера.
    Как проходит сериализация и десериализация
  - Библиотека OkHttp (встроена в Retrofit)
- Навигация между фрагментами/активити
  Cicerone, Jetpack navigation
- Многопоточность
  - Kotlin coroutines
  - RxJava
- DI

[Dependency injection](https://habr.com/ru/post/434380/) – внедрение зависимостей. Помогает писать менее зависимый код, значительно упрощает написание тестов.

Самые популярные библиотеки для внедрения зависимостей на Android это Toothpick, Dagger2, Koin, Hilt

- Service Locator
  [Service Locator](https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D0%BA%D0%B0%D1%82%D0%BE%D1%80_%D1%81%D0%BB%D1%83%D0%B6%D0%B1) - паттерн, используемый для получения зависимостей из общего хранилища. Отличается от DI тем, что самостоятельно не создает компонент, то есть не вызывает его конструктор.
- Single Activity (дописать)
  Отличная [статья](https://habr.com/ru/companies/redmadrobot/articles/426617/) про Single Activity
- Clean Architecture ([Чистая архитектура](https://nuancesprog.ru/p/11445/)). В ее основе чистое ядро и доменные сущности, независимые от платформы и фреймворков
- Тестирование приложения
  - Unit-тесты
    Тестируют отдельные классы и методы.
    Самые популярные библиотеки – JUnit, Mockito.
  - UI-тесты.
    Тестируют работу приложения в целом, имитируя действия реального пользователя. Библиотеки для UI тестов - Espresso, Kaspresso, Kakao
- [Material Design](https://material.io) - дизайн нативных android-интерфейсов, разработанный Google

#### Android Studio

- [Debug-меню](https://medium.com/@artem_shevchenko/android-studio-debugging-%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F-%D0%B8-%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8-658ee6dcc641). Инструмент в Android Studio, упрощающий нахождение багов в приложении
- Отладка приложений
  - Flipper
  - Proxyman
  - [Stetho](http://facebook.github.io/stetho/)
- Hotkey - с их помощью можно быстро переименовывать файлы, названия переменных, классов или методов. Можно увидеть все использования функции или класса, и много чего еще - [ссылка](https://medium.com/mindorks/11-android-studio-shortcuts-every-android-developer-must-know-a153e736e611)
- Эмуляторы - эмулирует Android на компьютере. Это полезно, если нужно проверить работу приложения на определенной версии системы, или на устройстве с большим/маленьким размером экрана. Позволяет задавать практически любую конфигурацию - менять версию Android, размер экрана, эмулировать камеру, местоположение.

#### ООП

- SOLID
    [Принципы SOLID](https://medium.com/webbdev/solid-4ffc018077da) помогут лучше понять ООП и применять его правильно

#### Git

- Нужно уметь использовать консоль и\или UI-клиент
  [Fork](https://git-fork.com)
- Нужно уметь работать с удаленным git-репозиторием
  - Уметь подключать к проекту хостинги git-репозиториев, например GitHub или GitLab
  - Умеет делать `merge request` и решать `merge conflict`, знает про `stash` и `cherry-pick`.

### Источники знаний

<details>
  <summary>Телеграм-каналы</summary>
  
- [Kotlin Adept Notes](https://t.me/kotlin_adept) (Канал нашего коллеги)
- [Android broadcast](https://t.me/android_broadcast)
- [Mobile Native](https://t.me/mobile_native)
- [Kotlin Broadcast](https://t.me/kotlin_broadcast)
- [Android Good Reads](https://t.me/droidgr)
- [Android Дичь](https://t.me/shitty_android)
- [Start Android](https://t.me/startandroid)
- [Android Live](https://t.me/android_live)
- [Android Guards Today](https://t.me/android_guards_today)
- [ProDev | Всё об Android разработке](https://t.me/droDev)
- [Devcolibri](https://t.me/dcolibri)
  
</details>

<details>
  <summary>Книги</summary>
  
- Bruce Eckel, Svetlana Isakova. [Atomic Kotlin](https://www.atomickotlin.com/atomickotlin/)
- Chet Haase. [Androids: The Team That Built the Android Operating System](https://www.amazon.com/Androids-Built-Android-Operating-System/dp/1737354810/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=)
- Дмитрий Жемеров. [Kotlin в действии](https://www.labirint.ru/books/612984/)
- Thomas Nield. [Learning RxJava](https://www.oreilly.com/library/view/learning-rxjava/9781787120426/)
- Джошуа Блох. [Java. Эффективное программирование](https://www.litres.ru/book/dzhoshua-bloh/javatm-effektivnoe-programmirovanie-48411247/)
- John Ousterhout. [A Philosophy of Software Design](https://www.amazon.com/Philosophy-Software-Design-John-Ousterhout/dp/1732102201)
- Marcin Moskala. [Effective Kotlin](https://leanpub.com/effectivekotlin)
- Роберт Мартин. [Чистый код. Создание, анализ и рефакторинг](https://www.labirint.ru/books/642466/)
- Чад Фаулер. [Программист-фанатик](https://www.labirint.ru/books/647973/)
  
</details>

<details>
  <summary>Курсы</summary>
  
- [Курс от Doubletapp](https://www.youtube.com/playlist?list=PLQ09TvuOLytS_vYHtFHQzZJFcnbYCYF6x)
- [Уроки по разработке от Mail.ru](https://youtu.be/GmZEFB0is6Y) (видео) + [Курс по Android в Технополисе 2019](https://github.com/polis-vk/2019-android)
- [Школа мобильной разработки от Yandex](https://www.youtube.com/playlist?list=PLQC2_0cDcSKBNCR8UWeElzCUuFkXASduz)
- [Уроки по Android/Kotlin от SkillBranch](https://www.youtube.com/channel/UCWLKyJUZ32GJvSIisQjU3kw/playlists)
- [Бесплатный текстовый курс по Android разработке](https://github.com/ArturVasilov/AndroidSchool)

</details>
  
<details>
  <summary>Статьи</summary>
  
- [52 ресурса для начинающих и профессиональных Android-разработчиков](https://apptractor.ru/develop/51-resurs-dlya-nachinayushhih-i-professionalnyih-android-razrabotchikov.html)

</details>

## Level 3️: `Middle`

Middle-разработчик может сам спроектировать приложение, настроить среду и CI/CD. Имеет не только основные, но и смежные знания. Обучает стажеров.

### Софт-скиллы

- Умеет ставить задачи
- Умеет аргументировать свою позицию
- Адекватно воспринимает критику, исправляет ошибки
- Умеет давать обратную связь

### Хард-скиллы

<details>
  <summary>CI/CD</summary>
  
[Концепция непрерывной интеграции и доставки](https://medium.com/southbridge/ci-cd-%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B-%D0%B2%D0%BD%D0%B5%D0%B4%D1%80%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-f0626b9994c8)
  
</details>

<details>
  <summary>Работа с устройством</summary>
  
- GPS
- Камера
- Гироскоп
- NFC
- Микрофон
- Датчик света
- otg-порт
  
</details>

<details>
  <summary>Сервисы Google</summary>
  
- Firebase
- Google Maps
- Google Play
- Google Pay
  
</details>

<details>
  <summary>Безопасность</summary>
  
- Proguard, D8, R8
- Keystore
  
</details>

<details>
  <summary>Android Jetpack</summary>
  
- Databinding
- Compose
- CameraX
  
</details>

<details>
  <summary>Сервисы Google</summary>
  
- Firebase
- Google maps
- Google Play
- Google Pay
  
</details>

<details>
  <summary>Kotlin Multiplatform (KMP)</summary>
  
Kotlin Native
Targets/Source sets
Compose Multiplatform
  
</details>

### Знаешь эти инструменты

- Работа с HTTP/S — [OkHttp](https://square.github.io/okhttp/), [Retrofit](https://github.com/square/retrofit)
- Работа с WebSockets — [Scarlet](https://github.com/Tinder/Scarlet), [nv-websocket-client](https://github.com/TakahikoKawasaki/nv-websocket-client)
- Работа с БД — [Room](https://developer.android.com/topic/libraries/architecture/room), [Realm](https://github.com/realm/realm-java), [SQLDelight](https://github.com/cashapp/sqldelight)
- Логирование — [Timber](https://github.com/JakeWharton/timber)
- Работа с датами — [ThreeTenABP](https://github.com/JakeWharton/ThreeTenABP)
- Навигация — [Cicerone](https://github.com/terrakok/Cicerone), [Navigation Component](https://developer.android.com/guide/navigation/navigation-getting-started)
- Dependency Injection — [Toothpick](https://github.com/stephanenicolas/toothpick), [Koin](https://github.com/InsertKoinIO/koin), [Dagger2](https://github.com/google/dagger), [Hilt](https://developer.android.com/training/dependency-injection/hilt-android)
- Посмотреть утечки — [LeakCanary](https://github.com/square/leakcanary)
- Тесты — [Mockito](https://github.com/mockito/mockito), [Mockk](https://mockk.io), [AssertJ](http://joel-costigliola.github.io/assertj/assertj-core.html), [Kakao](https://github.com/agoda-com/Kakao), [Kaspresso](https://github.com/KasperskyLab/Kaspresso)
- Анализ кода — [ktlint](https://github.com/pinterest/ktlint), [detekt](https://github.com/arturbosch/detekt)
- Обработка потока данных — [RxJava](https://github.com/ReactiveX/RxAndroid), [Kotlin coroutines](https://kotlinlang.org/docs/coroutines-overview.html)
- Работа с изображениями — [Picasso](https://square.github.io/picasso/), [Glide](https://github.com/bumptech/glide), [Fresco](https://github.com/facebook/fresco)
- Debug — [Stetho](http://facebook.github.io/stetho/), [Chucker](https://github.com/ChuckerTeam/chucker), [Flipper](https://fbflipper.com), [Proxyman](https://proxyman.io)
- Проверка орфографии — [yaspeller](https://github.com/hcodes/yaspeller)
- Оптимизация и обфускация кода — Proguard, D8, R8

### Источники знаний

- [Большой список книг, каналов, библиотек](https://kotlin.link)
- [Блог Android developer](https://medium.com/androiddevelopers) на Medium
- [Блог Pro Android Dev](https://proandroiddev.com)
- [Android Developers Blog](https://android-developers.googleblog.com/)

## Level 4️: `Senior`

### Roadmap

- [TeamLead Roadmap](https://tlroadmap.io/) – как развиваться самому в качестве TeamLead. Roadmap от Егора Толстого.
