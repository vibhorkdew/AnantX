output "vpc_id" {
  value = aws_vpc.anantx_vpc.id
}

output "subnet_id" {
  value = aws_subnet.public_subnet.id
}

output "igw_id" {
  value = aws_internet_gateway.anantx_igw.id
}

output "route_table_id" {
  value = aws_route_table.public_rt.id
}