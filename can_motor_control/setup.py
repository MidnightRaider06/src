from setuptools import find_packages, setup

package_name = 'can_motor_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'python-can'],
    zip_safe=True,
    maintainer='abhinavkota06',
    maintainer_email='abhinavkota06@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'can_motor_control_node = can_motor_control.can_motor_control_node:main'
        ],
    },
)
