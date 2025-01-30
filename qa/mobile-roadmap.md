# План погружения в мобильное тестирование

Если ты уже работаешь в тестировании, но впервые сталкиваешься с мобильным направлением, этот план — твой помощник. Здесь собраны материалы, которые помогут понять основы, освоить инструменты и научиться тестировать мобильные приложения эффективно.  

Этот план не претендует на универсальность и не ставит цели охватить всё возможное. Скорее, это твой гибкий помощник, благодаря которому ты быстрее почувствуешь себя уверенно в мобильном тестировании. Ты можешь использовать его как отправную точку, добавлять собственные находки и адаптировать под свои задачи. 

## Введение в мобильное тестирование
- [Типы мобильных приложений](https://vladislaveremeev.gitbook.io/qa_bible/mobilnoe-testirovanie/tipy-mobilnykh-prilozhenii) — статья рассказывает о различных типах мобильных приложений (нативные, веб- приложения и гибридные), их особенностях, преимуществах и недостатках с точки зрения тестирования. 
- [Мобильные приложения и их Мобильные приложения и их тестировщики: all you need to know](https://habr.com/ru/company/tdb/blog/337234/) — очень подробная и интересная статья, которая дает обзор тестирования мобильных приложений, рассматривая ключевые аспекты, такие как особенности платформ, типы тестирования и основные инструменты
- [5 принципов тестирования мобильных приложений](https://habr.com/ru/articles/244345/) — старая, но все еще актуальная статья о ключевых моментах, которые следует учитывать при тестировании мобильных приложений.
- [Мнемоники мобильного тестирования](https://software-testing.ru/library/testing/mobile-testing/2942-mobile-app-testing-mnemonic) — советы по запоминанию важных аспектов тестирования.
- [Особенности планирования работ по тестированию мобильных приложений](https://quality-lab.ru/blog/key-principles-of-planning-mobile-applications-testing/)

## Платформы мобильных приложений
- [Основные различия Android и iOS](https://github.com/VladislavEremeev/QA_bible/blob/master/mobilnoe-testirovanie/osnovnye-razlichiya-android-ios.md) — короткая статья, где тезисно сравниваются особенности этих ОС
- [Философия iOS vs ANDROID | РАЗБОР](https://www.youtube.com/watch?v=KnINsmXT9_c) — видео на эту же тему
- [Кросс-платформенное тестирование мобильных приложений: особенности, инструменты и решения](https://habr.com/ru/companies/domclick/articles/859546/) — статья раскрывает тему особенностей тестирования iOS и Android.

### Android
- [Архитектура Android](https://github.com/VladislavEremeev/QA_bible/blob/master/mobilnoe-testirovanie/android/arkhitektura-android-os.md) — статья рассматривает архитектуру операционной системы Android, включая её основные компоненты, уровни и взаимодействие между ними, что помогает тестировщикам лучше понимать разработчиков и принципы работы мобильных приложений
- [Архитектура приложений на Android](https://github.com/VladislavEremeev/QA_bible/blob/master/mobilnoe-testirovanie/android/arkhitektura-android-application.md) — здесь про архитектуру приложений на Android, включая их основные компоненты и жизненный цикл Activity

### iOS
- [Архитектура iOS](https://github.com/VladislavEremeev/QA_bible/blob/master/mobilnoe-testirovanie/ios/arkhitektura-ios.md) 
- [Архитектура приложений на iOS](https://github.com/VladislavEremeev/QA_bible/blob/master/mobilnoe-testirovanie/ios/arkhitektura-ios-application.md) 
- [Учебное пособие по тестированию приложений iOS: руководство и автоматизация](https://www.guru99.com/ru/getting-started-with-ios-testing.html) — руководство по тестированию iOS- приложений, охватывающее как ручные, так и автоматизированные подходы, с акцентом на проверку совместимости на разных устройствах и версиях iOS. Открывать с впн.

## Дизайн мобильных приложений
Для поддержания консистентности всех компонентов, которые используются в мобильных приложениях Контура, используются дизайн-система.

> Дизайн-система — это набор правил, принципов и инструментов, которые помогают поддерживать единство дизайна цифровых продуктов или услуг. Основная цель дизайн-системы — обеспечить целостный и последовательный пользовательский опыт на всех платформах и устройствах. Она формирует общий язык и набор стандартов для дизайнеров, разработчиков и маркетологов, что сокращает время и усилия, необходимые для создания новых продуктов.

Во многих компаниях есть своя дизайн-система; следует обязательно узнавать о ее наличии.

Ниже перечислим материалы, которые будут полезны для ознакомления с основными понятиями, а также для понимания, на каких основополагающих правилах строится любая дизайн-система
- [UI-элементы и жесты в мобильных приложениях](https://habr.com/ru/companies/youla/articles/540768/) — статья рассматривает основные термины и понятия, связанные с дизайном мобильных приложений, описывая ключевые элементы интерфейса
- [Гайдлайны Google Material и Apple Human Interface](https://www.youtube.com/watch?v=28m34MR_g2c) — полезное видео про гайдлайны
- [iOS и Android в дизайне](https://www.youtube.com/watch?v=eBlPBoCStp4) — еще одно видео
- [Гайдлайны Android и iOS](https://software-testing.ru/library/testing/mobile-testing/3103-android-and-ios-guidelines)
- [Material Design](https://m3.material.io/) 
- [Human Interface](https://developer.apple.com/design/human-interface-guidelines/)

## Проверки, специфичные для мобильных приложений

- [Нефункциональные проверки мобильных приложений ](https://habr.com/ru/companies/kuper/articles/707280/)
- [Мобильное тестирование: чек-лист и основные подходы](https://software-testing.ru/library/testing/mobile-testing/3518-mobile-app-testing-checklist) — структурированная информация о необходимых проверках при тестировании мобилок
- [Тестирование push-уведомлений](https://habr.com/ru/articles/706190/)
- [Тестирование push-уведомлений (часть 2)](https://habr.com/ru/articles/811297/)
- [Accessibility-тестирование мобильных приложений](https://rutube.ru/video/5134740332c20a804cafc858a319caf5/) — видео про тестирование доступности 
- [Пермишены (permissions) для тестировщика: зачем нужно, что такое и как с этим работать](https://habr.com/ru/articles/816951/)

### Тестирование фрагментации

Когда речь идет о фрагментации в мобильном тестировании, в первую очередь подразумевается Android. Эта ОС представлена огромным количеством устройств с разными версиями системы, диагоналями и разрешениями экранов, аппаратными возможностями и даже наличием или отсутствием Google-сервисов (например, Huawei). В отличие от iOS, где экосистема более контролируема, в Android разнообразие устройств создает дополнительные сложности для тестирования.

- [Почему фрагментация на Android — это хорошо](https://androidinsider.ru/os/pochemu-fragmentacziya-na-android-eto-horosho.html) — статья описывает само понятие фрагментации и подходы к тестированию в Android с ее учетом
- [Особенности тестирования Android без Google-сервисов](https://habr.com/ru/companies/surfstudio/articles/559106/) — тема, которую стоит осветить отдельно. Про устройства Huawei и AppGallery
- [Фермы мобильных устройств](https://habr.com/ru/companies/microsoft/articles/333606/) — Зачем использовать фермы, их возможности. Отметим, что в нашей команде фермы не используются по соображениям безопасности.

#### Выбор мобильных устройств для тестирования

Отдельно хочется затронуть тему выбора мобильных устройств для тестирования. Как правильно выбрать размеры экранов, версии ОС, модели устройств? 

- [Как выбрать мобильные девайсы для тестирования и не налажать](https://habr.com/ru/companies/otus/articles/509596/) — небольшая статья, главная мысль которой в том, что при выборе устройств мы опираемся на статистику, внешнюю или внутреннюю.
- [Покрытие девайсов](https://github.com/VladislavEremeev/QA_bible/blob/master/mobilnoe-testirovanie/pokrytie-devaisov.md)
- [Выбор мобильных устройств: пошаговая инструкция для начинающих QA. Часть I](https://software-testing.ru/library/testing/mobile-testing/3433-choosing-mobile-devices-1)
- [Выбор мобильных устройств: пошаговая инструкция для начинающих QA. Часть II](https://software-testing.ru/library/testing/mobile-testing/3434-choosing-mobile-devices-2)
- [AppMetrica](https://yandex.ru/adv/edu/materials/summary-appmetrica) — один из инструментов, который мы используем для сбора статистики и не только. Ознакомься с инструментом, чтобы понимать, для чего он и какие задачи помогает решить

## Инструменты мобильного тестировщика 
### Эмуляторы и симуляторы

- [Отличия эмуляторов и симуляторов](https://testengineer.ru/ehmulyatory-i-simulyatory-v-chem-raznica/) - сначала немного теории
- [Simulator iOS XCode](https://www.youtube.com/watch?v=LimscelXdFI)
- [Android Studio](https://github.com/VladislavEremeev/QA_bible/blob/master/mobilnoe-testirovanie/android/android-studio-dlya-qa.md) - интегрированная среда разработки (IDE) для работы с платформой Android. Позволяет работать с эмуляторами

#### Genymotion

- [Официальное руководство пользователя Genymotion](https://docs.genymotion.com/desktop/) - Подробная документация от разработчиков, охватывающая все аспекты использования Genymotion, включая установку, настройку и основные функции.
- [Руководство по использованию Genymotion для новичков](https://fb.ru/article/498574/2023-genymotion-kak-polzovatsya-podrobnoe-rukovodstvo-dlya-novichkov) - Статья, подробно описывающая процесс установки и настройки Genymotion, а также решение распространенных проблем, с которыми могут столкнуться новички.
  - [Мы спасены! Genymotion — забудьте про вашего медленного эмулятора Android](https://habr.com/ru/articles/185096) - Статья на Хабре, рассказывающая о преимуществах использования Genymotion по сравнению с другими эмуляторами Android.

### Работа с логами

- [Снятие логов на Android и iOS](https://habr.com/ru/companies/redmadrobot/articles/687184/)
- [Logcat](https://habr.com/ru/articles/818751/): вывод логов системы и приложений Android

### Сервисы для доставки сборок тестировщикам

Зачастую в компаниях для доставки продуктов используются такие программы, как:


- [AppCenter](https://appcenter.ms/) - облачный сервис от Microsoft, который позволяет автоматизировать жизненный цикл приложений для iOS, Android, Windows и macOS. 
- [TestFlight](https://developer.apple.com/testflight/) - для бета тестирования на iOS 

В нашей компании используется собственный софт под названием AppDrive. 

### Снифферы трафика

- [Снифферы трафика и обзор Charles, Fiddler, Proxyman](https://www.youtube.com/watch?v=Q6fHTKAE0lk&utm_source=chatgpt.com)

Далее перечислим полезные маатериалы по работе с различными снифферами. Не нужно изучать материалы по каждому инструменту. Лучше выбрать один и пользоваться им.

#### Charles Proxy:

- [Официальный сайт](https://www.charlesproxy.com/)
- [Настройка Charles Proxy для тестирования мобильных приложений](https://testgroru/article27)
- [Видеоурок: "Установка и Настройка Charles Proxy и подключение смартфона"](https://www.youtube.com/watch?v=6DIrVKlu1t0)
- [Charles Proxy. Practice for QA Engineer](https://youtu.be/74mvpPOczgI?si=bqfkTD6JKIrtoHHZ)

#### Proxyman:

- [Официальная документация](https://docs.proxyman.io/)
- [Видеоурок: "Proxyman (проксимэн) - как установить, пользоваться, обзор..."](https://www.youtube.com/watch?v=Vuu_OIUq8xA)
- [Почему Proxyman — сын маминой подруги в мире снифферов](https://software-testing.ru/library/testing/testing-tools/3765-proxyman)

#### Fiddler

- [Первые шаги с Fiddler Classic](https://habr.com/ru/articles/533138/)
- [Fiddler = удобный сниффер + прокси сервер](https://habr.com/ru/articles/554562/)

### Ментальные карты

- [Mind Map в тестировании — или легкий способ тестировать сложные приложения](https://habr.com/ru/articles/515990/) - статья для понимания, что это за зверь
- В Контуре для построения мэпок мы используем инструмент [XMind](https://xmind.app/)

### Работа с API

- [Postman - основы тестирования](https://habr.com/ru/companies/vk/articles/750096/)

### Git

- [Git для тестировщиков](https://habr.com/ru/companies/intec_balance/articles/865098/)
- [Первый тренажер для изучения Git](https://learngitbranching.js.org/?locale=ru_RU)
  - [Второй тренажер для изучения Git](https://githowto.com/ru)

### Режим разработчика 

- [Режим разработчика на Android](https://lifehacker.ru/kak-vkluchitj-rezhim-razrabotchika-na-android/)
- [Режим разработчика на iOS](https://www.iphones.ru/iNotes/kak-vklyuchit-rezhim-razrabotchika-na-iphone-i-ipad-chto-delat-esli-takogo-razdela-net-v-nastroykah-03-13-2024)

## Полезные ресурсы

### Сайты

- <https://software-testing.ru> – русскоязычный сайт с библиотекой статей, форумом и полезными материалами.
- <https://www.ministryoftesting.com> – крупнейшее сообщество тестировщиков с форумами, событиями и статьями.
- <https://testguild.com> – сайт с подкастами и статьями по автоматизации тестирования, включая мобильные приложения.
- <https://www.browserstack.com/blog> – статьи о тестировании, фермах устройств и полезных инструментах.
- <https://github.com/VladislavEremeev/QA_bible/tree/master/mobilnoe-testirovanie> - тоже очень полезный ресурс для изучения мобильного и тестирования в целом

### Telegram каналы 

- [QA Guild](https://t.me/qa_guild) – полезные статьи, вакансии и обсуждения для тестировщиков.
- [Тестировщик ПО](https://t.me/software_testing_qa) – новости и советы по тестированию.
- <https://t.me/qatesting> - QA Telegram – канал с бесплатными курсами, статьями и обсуждениями для тестировщиков.
- [QA Automation Tips](https://t.me/qa_automation_tips) – канал, посвящённый автоматизации тестирования, в том числе мобильных приложений.

### Youtube каналы


- [Канал Артема Русова](https://www.youtube.com/@rusau) - здесь очень много полезной информации, в т.ч., [подборка для мобильных тестировщиков](https://wiki.skbkontur.ru/pages/viewpage.action?pageId=894127499) 
- [Software Testing by QA Valley](https://www.youtube.com/@QAVALLEY) – англоязычный канал с видео о тестировании, включая мобильные приложения.
- [QA TestLab](https://www.youtube.com/@QATestLab) – канал с полезными видео о тестировании веб- и мобильных приложений.
- [Automation Step by Step](https://www.youtube.com/@AutomationStepByStep) – уроки по инструментам автоматизации тестирования.

### Литература:


- «Тестирование мобильных приложений: руководство» — Алексей Баранцев.
- «Continuous Testing for Mobile» — Книга о непрерывном тестировании в контексте мобильных приложений.
- «The Art of Mobile App Testing» — Подробное руководство по мобильному тестированию с фокусом на сложные сценарии и автоматизацию.
- «Ключевые процессы тестирования» — Рекс Блек.
- «Mobile Testing Tips» — Карен Джонсон.
- «Тестирование dot com» – Роман Савин - Базовая книга по тестированию, включая мобильные приложения.
- «Testing Mobile Applications» – John Flanagan - Практическое руководство по тестированию мобильных приложений.
- «Mobile Testing Handbook» – Daniel Knott - Полное руководство по тестированию мобильных приложений.
- «Android Studio Development Essentials» – Neil Smyth - Основы работы с Android Studio, полезно для ручного и автоматизированного тестирования.

## Для общего кругозора мобильного тестировщика

Здесь собраны материалы для общего развития, чтобы знать, что такое существует. На проектах Контура мы пока это не используем.

### Покупки

- [Как начать тестировать подписки в Google Play и App Store](https://habr.com/ru/articles/873950/)
- [Тестирование покупок в Android-приложениях](https://vladislaveremeev.gitbook.io/qa_bible/mobilnoe-testirovanie/android/testirovanie-pokupok-v-android-prilozheniyakh)
- [Тестирование покупок в iOS-приложениях](https://vladislaveremeev.gitbook.io/qa_bible/mobilnoe-testirovanie/ios/testirovanie-pokupok-v-ios-prilozheniyakh)
- [Тестирование платежей: руководство по тестовым платежам в RuStore](https://vladislaveremeev.gitbook.io/qa_bible/mobilnoe-testirovanie/testirovanie-push-uvedomlenii)

### Скриншот тесты

- [Две стратегии скриншот-тестирования в мобильных проектах](https://apptractor.ru/info/articles/dve-strategii-skrinshot-testirovaniya-v-mobilnyh-proektah.html)
