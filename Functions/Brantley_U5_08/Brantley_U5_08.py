
def main():
    input_sqft = int(input('Sqft to paint? : '))
    input_price_paint = int(input('Price per gallon paint? : '))
    g_paint_required, hours_labor, cost_labor = gpr(input_sqft)
    cost_paint = costPaint(input_price_paint, g_paint_required)
    total_cost = totalCost(cost_labor, cost_paint)
    print('Gallons paint required: ', format(g_paint_required, ',.2f'), sep='')
    print('Hours of labor required: ', format(hours_labor, ',.2f'), sep='')
    print('Cost of paint: $', format(cost_paint, ',.2f'), sep='')
    print('Cost of labor: $', format(cost_labor, ',.2f'), sep='')
    print('Total Cost: $', format(total_cost, ',.2f'), sep='')

#input division of sqft and labor
def gpr(input_sqft):
   g_paint_required = (input_sqft/112)
   hours_labor = (input_sqft/112) * 8
   cost_labor = 35 * hours_labor
   return g_paint_required, hours_labor, cost_labor

def costPaint(input_price_paint, g_paint_required):
    return  input_price_paint * g_paint_required

def totalCost(cost_labor,cost_paint):
    return cost_labor + cost_paint
           
main()

