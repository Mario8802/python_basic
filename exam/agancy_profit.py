airlines = input()
ticket_count = int(input())
children_ticket_count = int(input())
net_adult_price = float(input())
service_fee = float(input())
                              # sorry for writing that much
children_ticket_price = net_adult_price * 0.30
adult_ticket_price_with_service_fee = net_adult_price + service_fee
children_ticket_price_with_service_fee = children_ticket_price + service_fee
total_sum_tickets = (ticket_count * adult_ticket_price_with_service_fee) \
                    + (children_ticket_count * children_ticket_price_with_service_fee)
profit = total_sum_tickets * 0.20
print(f"The profit of your agency from {airlines} tickets is {profit:.2f} lv.")