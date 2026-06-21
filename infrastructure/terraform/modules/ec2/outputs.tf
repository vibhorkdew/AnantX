output "anantbuy_public_ip" {
  value = aws_instance.anantbuy_node.public_ip
}

output "devsecops_public_ip" {
  value = aws_instance.devsecops_node.public_ip
}

output "anantx_public_ip" {
  value = aws_instance.anantx_node.public_ip
}
