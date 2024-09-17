import rclpy
from rclpy.node import Node
import can

class CANMotorControlNode(Node):
    def __init__(self):
        super().__init__('can_motor_control_node')
        #Initialize the CANBus interface with socketCAN
        try:
            self.bus = can.interface.Bus(channel='can0', bustype='socketcan')
            self.get_logger().info("CAN interface initialized successfully")
        except OSError:
            self.get_logger().error("Cannot initialize CAN interface. Check if can0 is set up properly.")
            return
        
        #Send a command to the motor every 0.1 seconds
        self.timer = self.create_timer(0.1, self.send_motor_command)
    
    def send_motor_command(self):
        # msg = can.Message(
        #     arbitration_id=0x1ABCDEFF, #29-bit identifier
        #     data=[0xA1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], # Example data
        #     is_extended_id=True #CAN2.0B extended frame

        # )
        # 141#0000000034AB0001

        msg = can.Message(
            arbitration_id=0x141, #11-bit identifier
            data=[0x00, 0x00, 0x00, 0x00, 0x34, 0xAB, 0x00, 0x01], # Example data
            is_extended_id=False #CAN2.0B non-extended frame

        )
        try:
            self.bus.send(msg)
            self.get_logger().info(f"Sent command: {msg}")
        except can.CanError as e:
            self.get_logger().error(f"Error sending CAN message: {e}")
    

def main(args=None):
    rclpy.init(args=args)
    node = CANMotorControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()