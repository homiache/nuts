package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(minimumCost([]int{6, 5, 7, 9, 2, 2}))
}

func minimumCost(cost []int) int {

	// Необходимая для покупки всех конфет сумма.
	var summ int

	// Текущая позиция самой дорогой нерассмотренной конфеты :)
	var currentMostExpensive int

	// Строго говоря, сортировать конфеты по цене имеет смысл только тогда,
	// когда конфет в магазине осталось больше двух.
	// Но мы не будем писать код для отдельных простейших случаев.
	sort.Slice(cost, func(i, j int) bool {
		return cost[i] > cost[j]
	})

	// Если в магазине осталось больше трёх конфет, то покупаем две самые дорогие,
	// поскольку нам иным способом их не получить, и забираем в подарок самую дорогую из оставшихся,
	// потому, что можем. :) Повторяем цикл.
	// Если в магазине осталось меньше тёх конфет, то мы вынуждены купить их все.
	for {
		if len(cost[currentMostExpensive:]) >= 3 {
			summ = summ + cost[currentMostExpensive] + cost[currentMostExpensive+1]
			currentMostExpensive += 3
		} else {
			for i := 0; i < len(cost[currentMostExpensive:]); i++ {
				summ = summ + cost[currentMostExpensive+i]
			}
			return summ
		}
	}
}
