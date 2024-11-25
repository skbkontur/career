# Рекомендации от Контура для iOS-разработчиков

*Ниже представлен roadmap от iOS-разработчиков Контура.
Этот roadmap не претендует на абсолютную правду и является субъективным мнением авторов. По такому пути мы шли сами и хотели бы видеть таких коллег рядом. В конце статьи вы также найдёте ссылки на роадмэпы от других авторов.*

## Level 1: `Intern`

Стажер должен обладать знаниями, чтобы пройти порог входа в профессию программиста и в промышленную разработку. Эти материалы помогут попасть на твою первую стажировку в компанию, пройти испытательный срок и получить опыт в iOS-разработке.

### Базовые знания

- Жизненный цикл приложения и жизненный цикл контроллера
<details>
  <summary>Концепции объектно-ориентированного программирования (ООП)</summary>
  
- типы данных
- переменные
- функции и методы
- наследование
- структуры
- классы и протоколы
  
</details>
<details>
  <summary>Базовые конструкции языка</summary>
  
- использование выражений `if/else`,
- оператора `switch`,
- циклов,
- инструкций `break`, `continue` и т.д.

</details>
<details>
  <summary>Структуры данных</summary>
  
- коллекции: массивы, множества и словари

</details>
<details>
  <summary>Система контроля версий</summary>
  
- [**для чего нужен Git**](https://git-scm.com/book/ru/v2)
- как его использовать
	- [**онлайн-тренажер раз**](https://learngitbranching.js.org/)
	- [**онлайн-тренажер два**](https://githowto.com/ru/)

</details>
<details>
  <summary>Проектирование программного обеспечения</summary>
  
- как организовать и оформить код для удобства чтения
- как реализовать паттерн проектирования Model View Controller и Model View ViewModel


</details>
<details>
  <summary>Работа с сетью</summary>
  
- как выполнять асинхронные вызовы API
- как хранить и извлекать сетевые данные
- как использовать формат JSON для взаимодействия с сервером

</details>

**Опционально**

- Локальное хранение данных: как использовать Core Data, Realm, Codable и User Defaults для локального хранения данных приложения.
- SwiftUI: как использовать фреймворк Apple для создания пользовательских интерфейсов, которые хорошо выглядят на всех устройствах.

### Источники

- [**The Swift Programming Language**](https://docs.swift.org/swift-book/) – официальное издание по языку программирования Swift от Apple.
- Серия книг от Apple познакомит с инструментами для iOS разработчика, базовыми концепциями программирования, и лучшими практиками. Плюс можно пройти практические упражнения и научиться создавать приложения с нуля.
    - [**Develop in Swift Fundamentals**](https://books.apple.com/ru/book/develop-in-swift-fundamentals/id1556365994)
    - [**Develop in Swift Explorations**](https://books.apple.com/ru/book/develop-in-swift-explorations/id1556366287)
    - [**Develop in Swift Data Collections**](https://books.apple.com/ru/book/develop-in-swift-data-collections/id1556365920)
- [**SwiftBook**](https://swiftbook.ru) – самая крупная русскоязычная платформа для обучения основам Swift.
- [**iOS App Dev Tutorial**](https://developer.apple.com/tutorials/app-dev-training/) – основы Xcode, SwiftUI и UIKit для создания нативных приложений. Интерактивное обучение от Apple.
- [**App Development Bootcamp**](https://www.udemy.com/course/ios-13-app-development-bootcamp/) – курс для обучения с 0 до начинающего iOS разработчика.
- [**iOS and Swift от Raywenderlich**](https://www.raywenderlich.com/ios/paths)(https://www.udemy.com/course/ios-12-and-swift-4-for-beginners-200-hands-on-tutorials) – курсы от [*Raywenderlich*](https://www.raywenderlich.com/ios) для обучения с 0 до начинающего iOS разработчика.

## Level 2: `Junior`

### Базовые знания

<details>
  <summary>Язык программирования Swift</summary>
  
- [**Classes and Structures**](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html) – классы и структуры, в чем их отличия
- [**Property Observers и Wrappers**](https://docs.swift.org/swift-book/LanguageGuide/Properties.html)– наблюдатели и обёртки свойства
- [**Enumerations**](https://docs.swift.org/swift-book/LanguageGuide/Enumerations.html) – перечисления ассоциативные/исходные значения
- [**Collection Types**](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html) – типы коллекций: массивы, множества и словари (`Array`, `Set`, `Dictionary`)
- [**Closures**](https://docs.swift.org/swift-book/LanguageGuide/Closures.html) – замыкания и списки захвата
- [**Protocols**](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html) – протоколы такие как `Codable`, `Equatable`, `Hashable`
- [Extensions](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/extensions/) - расширения типов
- [**Optional Chaining**](https://docs.swift.org/swift-book/LanguageGuide/OptionalChaining.html) – опциональные типы данных и опциональная последовательность
- [**ARC**](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html) – автоматический подсчёт ссылок
- [**Access Control**](https://docs.swift.org/swift-book/LanguageGuide/AccessControl.html) – атрибуты доступа, такие как `private` и `public`
- [Concurrency](https://developer.apple.com/documentation/swift/concurrency) - cтруктурированный параллелизм (`async`,`await`, `Task`, `MainActor`, `sendable`)
- [Generics](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/) - дженерики, ключевые слова `some` и `any`


</details>
<details>
  <summary>Создание приложений</summary>
  
- Компоненты фреймворка [**UIKit**](https://developer.apple.com/documentation/uikit/) для создания и управления пользовательскими интерфейсами
	- `UIView` и его основные компоненты `UIButton`, `UITextField`, `UILabel`
	- `UIViewController` + `Child`, `UITableView`, `UINavigationController`, `UIStackView`
	- `Auto Layout` для построения адаптивных интерфейсов вместе с `Compression Resistance`/`Content Hugging Priorities`.
- Компоненты фреймворка [SwiftUI](https://developer.apple.com/documentation/swiftui/)
	- `View`, `@ViewBuilder`, `ViewModifier` + основные компоненты `Text`, `Button`, `V/H/Z-Stack`, `List`
	- `@State`, `@Binding`, `@Published` - обёртки свойств и зачем они нужны
	- Протокол `ObservedObject`, обёртки `@StateObject`, `@ObservedObject`, `@EnvironmentObject`, понимание разницы между ними
- Компоненты фреймворка [**Foundation**](https://developer.apple.com/documentation/foundation) для разработки базового слоя функциональности приложений
	- хранение данных `UserDefaults`, `Keychain`
	- обработка текста  `Formatters`
	- вычисление даты и времени  `Date`
	- работа с сетью: `Error+Result`,  `URLSession`
- Работа с сетью: [**Moya**](https://github.com/Moya/Moya), [**Alamofire](https://github.com/Alamofire/Alamofire),** URLSession async
- Использование модулей и добавление новых зависимостей: `Cocoapods` / `Swift Package Manager`
- Архитектура для UIKit: `MVC` с использованием `ChildViewController`, `MVVM`. Подходы с использованием `Data Driven ViewControllers(Props)`, `Coordinator` или `FlowController`
- Архитектура для SwiftUI: `MVVM` или `MV/MV State`
- [**Шаблоны и паттерны проектирования**](https://refactoring.guru/design-patterns/catalog)
	- [Singleton](https://refactoring.guru/design-patterns/singleton)
	- [Command](https://refactoring.guru/design-patterns/command)
	- [Factory Method](https://refactoring.guru/design-patterns/factory-method)
	- [Observer](https://refactoring.guru/design-patterns/observer)
	- [Delegation](https://www.swiftbysundell.com/articles/delegation-in-swift/)
- Разработка на основе TDD (Test Driven Development), Unit Testing, UI Testing
	- [Unit Testing Best Practices on iOS with Swift](https://www.vadimbulavin.com/unit-testing-best-practices-on-ios-with-swift/)
	- [Тестирование приложений: описание и чек-лист](https://ru.hexlet.io/blog/posts/testirovanie-prilozheniy-opisanie-i-chek-list)
	- [Начинаем писать тесты (правильно)](https://ru.hexlet.io/blog/posts/how-to-test-code)
	- [Test doubles in Swift: dummies, fakes, stubs, and spies.](https://mokacoding.com/blog/swift-test-doubles/)
	- [Курс: TDD. Unit Testing](https://swiftbook.ru/content/25-index/)
- RxSwift или Combine — чтение кода, использование операторов и семантичных сущностей.
- Основы [**Grand Central Dispatch**](https://developer.apple.com/documentation/dispatch) - многопоточное программирование, основные понятия и методы

</details>
<details>
  <summary>Инструменты и процессы</summary>
  
- Xcode
- Система контроля версий git и основные команды push, pull, commit, tags, merge/pull request, rebase, merge, cherry-pick, stash
- Профилирование и дебаг: поиск утечек памяти, циклов, дебаг UI, брейкпоинты, работа с консолью
- Принципы ООП, SOLID, KISS, DRY, YAGNI и т.п.

</details>
<details>
  <summary>Архитектуры</summary>
  
- [**iOS Architecture Patterns**](https://medium.com/ios-os-x-development/ios-architecture-patterns-ecba4c38de52) – поверхностный обзор архитектур
- [**MVC is not your problem**](https://www.youtube.com/watch?v=A1vzcxR-Ss0) — доклад о том, как делать MVC, не делая его massive.
- [**Правильный MVC**](https://www.youtube.com/watch?v=J8u-tIt5wo4) — как справиться с MVC. Доклад от Redmadrobot
- [**Awesome iOS architecture**](https://github.com/onmyway133/awesome-ios-architecture) – репозиторий с шуточным проектом по составлению новых акронимов "лучших iOS архитектур". Но в Readme проекта есть список полезных материалов по разным архитектурам.
	- [**MVC: Model View Controller**](https://rambo.codes/posts/2020-02-20-mvc-with-sugar) – доходчиво о MVC ([видео](https://www.youtube.com/watch?v=ZShE3toDPIk))
	- [**MVP: Model View Presenter**](https://blog.moove-it.com/going-from-mvc-to-mvp-on-ios/) – от MVC к MVP
	- [**MVVM: Model View ViewModel**](https://www.objc.io/issues/13-architecture/mvvm/) – введение в MVVM
	- [**Viper**](https://github.com/strongself/The-Book-of-VIPER) – книга от Rambler
- [**Математические основы Auto Layout**](https://habr.com/ru/company/oleg-bunin/blog/437584/) – работа в Auto Layout относительно простым языком

</details>

### Источники

- [**iOS-разработка на Coursera**](https://ru.coursera.org/specializations/ios-dev) – бесплатный русскоязычный курс по iOS-разработке
- [**Raywenderlich.com**](https://www.raywenderlich.com/ios) – книги и материалы по iOS-разработке. Платная подписка дает доступ к обновляемым материалам.
- [**Swiftbook**](https://swiftbook.ru/courses/) курсы по подписке - русскоязычные курсы по основным темам, с доступной подачей
- [**Swift Language**](https://developer.apple.com/swift/) ([**в переводе**](https://swiftbook.ru/content/docs/)) – углубленное изучение Swift
    - [**whatsnewinswift.com**](https://www.whatsnewinswift.com/) – сравнение Swift по версиям
    - [**Swift Standard Library**](https://developer.apple.com/documentation/swift/swift_standard_library) – cтандартная библиотека aka [PureSwift](https://github.com/PureSwift)
- [**Coordinator and FlowController**](https://github.com/onmyway133/blog/issues/106)
- [**Как работать с сетью правильно**](https://www.youtube.com/watch?v=7HtE3Ci78nU) — доклад от Сбербанка. URLSession и нативные подходы к работе с сетью.
- [100 Days of SwiftUI](https://www.hackingwithswift.com/100/swiftui) - обучение основам SwiftUI от Пола Хадсона (Hacking with Swift)
- [Advanced Combine Publishers & Subscribers](https://www.youtube.com/watch?si=0rWk7kpLJmRVOFD4&v=RUZcs0SWqnI&feature=youtu.be) - разбор работы с Combine
- Видео с WWDC про [async](https://developer.apple.com/videos/all-videos/?q=async) и [structured concurrency](https://developer.apple.com/videos/all-videos/?q=structured%20concurrency) - там есть почти вся нужная информация
- [Туториалы от sparrowcode](https://sparrowcode.io/ru)
- [**SwiftUI Property Wrappers**](https://swiftuipropertywrappers.com/)

## Level 3: `Middle`

Миддл разработчик способен за разумное время вникнуть в проект, вносить изменения в код, не ломая при это существующие сценарии. Может реализовывать фичи средней сложности, затрагивающие небольшое число компонентов. Умеет работать с существующим CI/CD и при необходимости вносить небольшие изменения. Понимает, как устроено создание сборок на iOS (certificates, app id, provisioning profiles).

### Базовые знания

<details>
  <summary>Язык программирования Swift</summary>
  
- Отличия между классами, акторами и структурами и понимание о том, что из них следует использовать
- Создание перечислений, структур, классов и протоколов
- Функциональное программирование, использование замыканий (trailing, auto, escaping closures)
- Понимание, как создаются и удаляются объекты с помощью автоматического подсчета ссылок (ARC)
- Понимание, потенциальной возможности возникновения сильного ссылочного цикла в замыканиях и переменных класса
- Swift - как протокольно-ориентированный язык программирования, применение таких протоколов, как Equatable, Comparable, Sequence
- Функционально-реактивное программирование (RxSwift, RxCocoa, Combine)
- Error Handling - ошибки программирования, ошибки пользовательского ввода, асинхронные ошибки
- [Макросы](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/macros/) в Swift (опционально)

</details>
<details>
  <summary>Создание приложений</summary>
  
- Компоненты фреймворка [UIKit](https://developer.apple.com/documentation/uikit/): UISplitViewController, UICollectionView, жизненный цикл UIView.
- Auto Layout - Адпативный текст и UI, Size Classes, создание ограничений в коде, понимание Layout Engine, иерархии представлений
- SwiftUI: жизненный цикл View, View Identity, понимание как и когда перерисовывается view
- Взаимодействие между UIKit и SwiftUI (`UIViewControllerRepresentable`, `UIViewRepresentable`, `UIHostingController`, `UIHostingConfiguration`)
- Сетевой слой приложения: реализация взаимодействия с сетью, основа сетевого уровня, HTTP, REST, `NSURLSession`, сериализация JSON, тестирование запросов
- Уровень хранения данных приложения: plist, NSUserDefaults/Keychain, File/Disk storage, CoreData
- Архитектура: MVC, MVVM, MVP, VIPER, MV (SwiftUI), подход Clean Architecture
- Дизайн паттерны и принцип SOLID
- CoreAnimation, Drawing
- [Grand Central Dispatch](https://developer.apple.com/documentation/dispatch) – многопоточное программирование, последовательные и параллельные очереди, основной поток, фоновый поток
- [Concurrency](https://developer.apple.com/documentation/swift/concurrency) - cтруктурированный параллелизм (`TaskGroup`, `TaskSequence`, `Checked/Unsafe-Continuation`, `actor`, `TaskPriority`) и как он работает внутри, cooperative thread pool, акторы, управление памятью в задачах (ARC), отмена задач, actor hopping и другие проблемы акторов
- Пуш уведомления
- TDD (Test Driven Development), Unit Testing, UI Testing
- Локализация приложений - String Catalogs или другие фреймворки
- [Observation Framework](https://developer.apple.com/documentation/observation) и [SwiftData](https://developer.apple.com/documentation/swiftdata) (опционально)
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) и [App Intents](https://developer.apple.com/documentation/appintents) (опционально)


</details>
<details>
  <summary>Инструменты и процессы</summary>
  
- CodeReview, Design Review
- Xcode Intruments и LLDB - применение на практике для анализа проблем и отладки
- Системы контроля версий git, GitLab
- CI (Continuous integration), CD (Continuous Delivery) - инициация сборок, инструменты и сервисы, GitLab CI, Fastlane


</details>

## Список полезных и интересных материалов

<details>
  <summary>Периодические материалы</summary>
  
- [**https://podlodka.io/**](https://podlodka.io) — подкаст обо всём
- [**https://iosdevweekly.com**](https://iosdevweekly.com/) — недельный дайджест мира iOS/macOS разработки

</details>
<details>
  <summary>Блоги</summary>
  
- [**https://objc.io/**](https://objc.io/) — статьи и видео
- [**https://www.swiftbysundell.com/**](https://www.swiftbysundell.com/) — блог и подкаст, хорошие статьи по базовым материалам
- [**https://nshipster.com**](https://nshipster.com/) — блог с глубокими знаниями и разбором от инженера Apple
- [**https://www.avanderlee.com**](https://www.avanderlee.com/) — блог с хорошим контентом на разные темы.
- [**https://www.pointfree.co/**](https://www.pointfree.co/) — видео, есть бесплатные. Функциональные подходы.
- [**https://useyourloaf.com**](https://useyourloaf.com/) — отличный блог и книга про AutoLayout. Контент книги = статьи из блога.
- [**https://refactoring.guru/ru**](https://refactoring.guru/ru) - отличный сайт, есть книга. Паттерны ООП, разбор рефакторинга, примеры кода.
- [**https://www.hackingwithswift.com**](https://www.hackingwithswift.com/) — хороший контент. Первый выбор для поиска типичных решений вместо stackoverflow
- [https://sarunw.com/](https://sarunw.com/) — емко, четко, по делу, и приятный сайт
- [@SwiftfulThinking](https://www.youtube.com/@SwiftfulThinking/videos) и [@seanallen](https://www.youtube.com/@seanallen/videos) - неплохие ютуб-каналы, актуальный контент
- [WWDC Notes](https://www.wwdcnotes.com) - краткий обзор видео и новостей с WWDC
- Ещё блоги: [https://swiftrocks.com](https://swiftrocks.com/), [https://www.vadimbulavin.com](https://www.vadimbulavin.com/), [https://byby.dev/ios](https://byby.dev/ios)


</details>
<details>
  <summary>Статьи</summary>
  
- [**Поверхностный обзор архитектур**](https://medium.com/ios-os-x-development/ios-architecture-patterns-ecba4c38de52)
- [**Математические основы AutoLayout**](https://habr.com/ru/company/oleg-bunin/blog/437584/)
- [**MVC, и как его можно улучшить**](https://rambo.codes/posts/2020-02-20-mvc-with-sugar).
Отличная статья про FlowController, Child controllers. Используем часто в Контуре.
- [**FlowController против Coordinator**](https://github.com/onmyway133/blog/issues/106).
В Контуре мы перешли от координаторов к FlowController.
- [**Building Large-Scale Apps with SwiftUI: A Guide to Modular Architecture**](https://azamsharp.com/2023/02/28/building-large-scale-apps-swiftui.html)
- [**Memory management when using async/await in Swift**](https://www.swiftbysundell.com/articles/memory-management-when-using-async-await/)

</details>
<details>
  <summary>Книги</summary>
  
- [**App Architecture**](https://www.objc.io/books/app-architecture/) – книга по архитектурам с примерами
- [**Книги на objc.io**](https://www.objc.io/books)
- [**Разные книги с крутым контентом**](https://store.raywenderlich.com/)
Для начала в iOS хорошая iOS Apprentice.
- [**Книги от Mattt (NSHipster)**](https://flight.school/)

</details>
<details>
  <summary>Swift</summary>
  
- [**Перевод**](https://swiftbook.ru/content/docs/) официальной книги [**Swift от Apple**](https://developer.apple.com/swift/)
- [**Сравнение фич swift по-версиям**](https://www.whatsnewinswift.com/)
- [**Стандартная библиотека Swift**](https://developer.apple.com/documentation/swift/swift_standard_library)

</details>
<details>
  <summary>RxSwift и Combine</summary>
  
- [**RxSwift Playground**](https://github.com/ReactiveX/RxSwift/blob/master/Documentation/Playgrounds.md)
- [**отличная книга по RxSwift с примерами**](https://store.raywenderlich.com/products/rxswift)
- [**топ ошибок при использовании RxSwift**](http://adamborek.com/top-7-rxswift-mistakes/)
- [**RxSwift to Combine Cheatsheet**](https://github.com/CombineCommunity/rxswift-to-combine-cheatsheet)
- [**Using Combine**](https://heckj.github.io/swiftui-notes/index.html)

</details>
<details>
  <summary>WWDC must watch</summary>
  
- [**Testing Tips & Tricks**](https://developer.apple.com/videos/play/wwdc2018/417/)
- [**iOS Memory Deep Dive**](https://developer.apple.com/videos/play/wwdc2018/416/)
- [**Understanding Crashes and Crashlogs**](https://developer.apple.com/videos/play/wwdc2018/414/)
- [Demistify SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10022/) и [Demistify SwiftUI performance](https://developer.apple.com/videos/play/wwdc2023/10160/)
- [Efficiency awaits: Background tasks in SwiftUI](https://developer.apple.com/wwdc22/10142)

</details>
<details>
  <summary>Доклады</summary>
  
- [**MVC is not your problem**](https://www.youtube.com/watch?v=A1vzcxR-Ss0) — доклад о том, как делать MVC, не делая его massive.
- [**Правильный MVC**](https://www.youtube.com/watch?v=J8u-tIt5wo4) — как справиться с MVC. Доклад от Redmadrobot
- [**Как работать с сетью правильно**](https://www.youtube.com/watch?v=7HtE3Ci78nU) — доклад от Сбербанка. URLSession и правильные подходы к работе с сетью.

</details>
<details>
  <summary>Интересные каналы Telegram</summary>
  
- [https://t.me/iosdev](https://t.me/iosdev)
- [https://t.me/iosmakesmehate](https://t.me/iosmakesmehate)
- [https://t.me/swift_ioss](https://t.me/swift_ioss)
- [https://t.me/iosgt](https://t.me/iosgt)
- [https://t.me/iosgr](https://t.me/iosgr)
- [https://t.me/sparrowcode](https://t.me/sparrowcode)
- [https://t.me/swift_ui](https://t.me/swift_ui)
- [https://t.me/coffeeCodeEverywhere](https://t.me/coffeeCodeEverywhere)
- [https://t.me/apptractor](https://t.me/apptractor)


</details>

## Level 4: `Senior`

### Roadmap

- [**TeamLead roadmap**](https://tlroadmap.io/) – как развиваться самому в качестве тимлида.
Роадмэп от Егора Толстого

### Other Roadmaps

Здесь представлены популярные маршруты знаний от разных авторов.
Их цель – дать представление об iOS-разработке и помочь сориентироваться в умениях и навыках.

- [**iOS developer roadmap**](https://gist.github.com/azimin/a44086ef3e2d5992aa411b8aa60d05a3) от [Александра Зимина](https://twitter.com/ZiminAlex?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)
- [**Swift developer roadmap**](https://trello.com/b/hLGyiEEE/swift-developer-roadmap) от [Ronan Rodrigo](https://twitter.com/ronanrodrigodev)
- [**iOS developer roadmap**](https://github.com/BohdanOrlov/iOS-Developer-Roadmap/blob/master/RoadmapProject/Script/Generated/ROADMAP.md) от [Богдана Орлова](https://twitter.com/bohdan_orlov)
- [**Таблица умений iOS-разработчика**](https://swiftbook.ru/post/tutorials/ios-deveoper-table-skillz/) от [SwiftBook](https://swiftbook.ru)