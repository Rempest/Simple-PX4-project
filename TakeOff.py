import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class CrazyFile(Node):
    def __init__(plus):
        super().__init__("CrazyFile")
        plus.publisher = plus.create_publisher(Twist, 'crazy_file', 10)
        plus.timer = plus.create_timer(1, plus.timer_crazyfile)
    def timer_crazyfile(plus):
        msg = Twist()
        msg.linear.x = 1.0
        msg.linear.y = 0.0
        msg.linear.z = 3.0
        plus.publisher.publish(msg)
        plus.get_logger().info(f'Отправлено: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}')
    def most(args = None):
        rclpy.init()
        node = CrazyFile()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    CrazyFile.most()
