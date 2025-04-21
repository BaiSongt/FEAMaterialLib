from material import IsotropicMaterial, MaterialBehavior

def main():
    # 创建一个钢材料的实例
    steel = IsotropicMaterial(
        name="Q235钢",
        density=7850,  # kg/m³
        thermal_conductivity=50,  # W/m·K
        specific_heat=460,  # J/kg·K
        behavior=MaterialBehavior.ELASTO_PLASTIC,
        youngs_modulus=210e9,  # Pa
        poissons_ratio=0.3,
        yield_strength=235e6,  # Pa
        ultimate_strength=400e6,  # Pa
        description="普通碳素结构钢"
    )

    # 打印材料信息
    print("材料基本信息：")
    print(steel)
    print("\n材料详细属性：")
    properties = steel.get_properties()
    for key, value in properties.items():
        print(f"{key}: {value}")

    # 获取弹性属性
    print("\n弹性属性：")
    elastic_properties = steel.get_elastic_properties()
    for key, value in elastic_properties.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
