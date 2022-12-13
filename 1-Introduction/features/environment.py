
def before_all(context):
    print('Before all executed')


# before every scenario
def before_scenario(context, scenario):
    print(f'Before scenario {scenario.name} executed')


# after every feature
def after_feature(context, feature):
    print(f'After feature {feature.name} executed')
