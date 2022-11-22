

DATA_STATES = {
            0: "К какому типу пользователей вы относитесь?",
            1: "Укажите цель:",
            2: "Укажите ваш уровень владения знаниями анализа:",
            3: "Укажите площадь исследуемых территорий: ",
            4: "Ограничен ли ваш бюджет?",
            5: "Имеются ли данные предыдущих ваших анализов?",
            6: "Имеются ли у вас формализованные данные о полях?",
            7: "Цель вашего исследования:",
            8: "Обладаете ли вы высоким уровнем знаний в области анализа растительности?",
            9: "Рекомендуется проводить личный осмотр, "
               "трата средств на информационные средства нецелесообразна!",
            10: "Какой тип системы вы предпочитаете?",
            11: "Рекомендуется проводить анализ с помощью ArcGIS PRO и индекса вегетации SAVI!",
            12: "Рекомендуется проводить анализ с помощью EOS Crop Monitoring и индекса вегетации SAVI!",
            13: "Рекомендуется проводить анализ с помощью QGIS и индекса вегетации SAVI",
            14: "Рекомендуется проводить изучение данных с помощью EOS Crop Monitoring с применением индексов"
                " вегетаций NDVI, NDRE",
            15: "Ограничен ли ваш бюджет?",
            16: "Рекомендуется использование EOS Crop Monitoring",
            17: "Ограничен ли ваш бюджет?",
            18: "Необходимо ли исследование с учетом различных типов индексов вегетации?",
            19: "Рекомендуется проводить анализ с использованием веб-сервиса OneSoil и индекса вегетации NDVI",
            20: "Рекомендуется проводить анализ с помощью ArcGIS PRO и "
                "индексов вегетации NDVI, NDRE с данные прошлых анализов!",
            21: "Рекомендуется проводить анализ с помощью QGIS и индексов вегетации NDVI NDRE с данными "
                "прошлых анализов!",
            22: "Рекомендуется импортировать данные и осуществлять исследование с помощью ArcGIS PRO",
            23: "Рекомендуется импортировать данные и осуществлять исследование с помощью QGIS",
            24: "Имеются ли готовые снимки для анализа?",
            25: "Необходима ли оценка концентрации азота в растительности?",
            26: "Рекомендуется применение EarthExplorer для сбора данных, QGIS для анализа "
                "снимков и вычисления различных индексов вегетации!",
            27: "Рекомендуется применение QGIS для анализа снимков и вычисления различных индексов вегетации!",
            28: "Рекомендуется проводить анализ данных с помощью QGIS и индекса вегетации NDVI!",
            29: "Рекомендуется проводить анализ данных с помощью EOS Crop Monitoring и "
                "индексов вегетации NDVI, GNDVI",
        }

DATA_ANSWERS = {
            0: {"Агроном компании": 1, "Исследователь": 2, "Частный фермер": 3},
            1: {"Оценка состояния почвы": 4, "Оценка урожайности": 5, "Изучение статистики полей": 6},
            2: {"Высокий уровень знаний": 1, "Низкий / средний уровень знаний": 7},
            3: {"Более 1 Га": 8, "Менее 1 Га": 9},
            4: {"Бюджет не ограничен": 10, "Бюджет ограничен": 13},
            5: {"Данных предыдущих анализов не имеется": 14, "Данные предыдущих анализов имеются": 15},
            6: {"Формализованные данные о полях не имеются": 16, "Формализованные данные о полях имеются": 17},
            7: {"Оценка состояния почвы": 4, "Изучение статистики полей": 6, "Оценка урожайности": 18},
            8: {"Имеется высокий уровень знаний в области анализа растительности": 25,
                "Не имеется высокий уровень знаний в области анализа растительности": 19},
            10: {"Предпочтителен тип системы - десктоп": 11, "Предпочтителен тип системы – веб-сервис": 12},
            15: {"Бюджет не ограничен": 20, "Бюджет ограничен": 21},
            17: {"Бюджет не ограничен": 22, "Бюджет ограничен": 23},
            18: {"Необходим учет различных вегетационных индексов": 24, "Учет различных вегетационных"
                                                                        " индексов не нужен": 25},
            24: {"Готовых снимков для анализа не имеется": 26, "Готовые снимки для анализа имеются": 27},
            25: {"Учет оценки концентрации азота в растительности не нужен": 28,
                 "Учет оценки концентрации азота в растительности нужен": 29},
        }

DATA_FINISH = {i: 0 for i in range(len(DATA_STATES))}
check_anwser = [9, 11, 12, 13, 14, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29]
for i in check_anwser:
    # инициализация ответов
    DATA_FINISH[i] = 1