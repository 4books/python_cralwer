from user_agent import generate_user_agent, generate_navigator

if __name__ == '__main__':
    print(generate_user_agent(device_type='desktop'))
    print(generate_user_agent(os='win', device_type='desktop'))
    print(generate_user_agent(os=('mac', 'linux'), device_type='desktop'))

    navigator = generate_navigator()
    print(navigator)
    print(navigator['platform'])


