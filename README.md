# goit-algo-hw-05


### Висновок щодо швидкостей алгоритмів пошуку підрядка

#### Алгоритми
1. Боєра-Мура
2. Кнута-Морріса-Пратта (КМП)
3. Рабіна-Карпа

#### Швидкість алгоритмів для першого тексту

Текст: "article1.txt"

1. Боєра-Мура:
   - Час виконання з валідним значенням: 0.002097684016916901
   - Час виконання з невалідним значенням: 0.015777312975842506
2. Кнута-Морріса-Пратта (КМП):
   - Час виконання з валідним значенням: 0.0061810199986211956
   - Час виконання з невалідним значенням: 0.0061810199986211956
3. Рабіна-Карпа:
   - Час виконання з валідним значенням: 0.011783900001319125
   - Час виконання з невалідним значенням: 0.03796587901888415

#### Швидкість алгоритмів для другого тексту

Текст: "article2.txt"

1. Боєра-Мура:
   - Час виконання з валідним значенням: 0.0009874279785435647
   - Час виконання з невалідним значенням: 0.008201746008126065
2. Кнута-Морріса-Пратта (КМП):
   - Час виконання з валідним значенням: 0.0029272990068420768
   - Час виконання з невалідним значенням: 0.023917974991491064
3. Рабіна-Карпа:
   - Час виконання з валідним значенням: 0.005510106013389304
   - Час виконання з невалідним значенням: 0.05377115699229762

#### Загальні висновки

1. Для першого тексту, найшвидшим алгоритмом виявився Боєра-Мура.
2. Для другого тексту, найшвидшим алгоритмом виявився Боєра-Мура.
3. У цілому, найшвидшим алгоритмом виявився Боєра-Мура.

#### Рекомендації
1. На основі вимірювань часу виконання, рекомендується використовувати Боєра-Мура для подальших операцій з пошуком підрядка в текстах подібного типу.
2. Для великих текстів рекомендується провести додаткові тести з іншими алгоритмами та порівняти їх ефективність.