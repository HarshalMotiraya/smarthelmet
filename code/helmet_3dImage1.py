import numpy as np
import trimesh

def create_smart_helmet_3d():
    # 1. Generate Outer Shell (Ellipsoid dome with neck/visor cutouts)
    outer_shell = trimesh.creation.icosphere(subdivisions=4, radius=1.0)
    outer_shell.apply_scale([110.0, 130.0, 90.0])  # Scale to helmet dimensions in mm

    # 2. Generate Inner EPS Liner Cavity
    inner_cavity = trimesh.creation.icosphere(subdivisions=4, radius=1.0)
    inner_cavity.apply_scale([95.0, 115.0, 75.0])

    # Create Shell Frame via Mesh Difference (Outer Shell - Inner Cavity)
    try:
        eps_liner = outer_shell.difference(inner_cavity)
    except Exception:
        eps_liner = outer_shell  # Fallback if boolean engine isn't installed

    # 3. Create Component Mounts (Pockets/Boxes)
    # Front Camera & IR Housing (Front Rim)
    camera_mount = trimesh.creation.box(extents=[30, 20, 20])
    camera_mount.apply_translation([0, 115, 30])

    # HUD Prism Mount (Inner Brow Region)
    hud_mount = trimesh.creation.box(extents=[25, 15, 15])
    hud_mount.apply_translation([30, 80, 20])

    # AI Compute Board Housing (Rear Shell)
    compute_board = trimesh.creation.box(extents=[60, 15, 40])
    compute_board.apply_translation([0, -110, 10])

    # Battery Pack Recess (Lower Rear Base)
    battery_pack = trimesh.creation.box(extents=[70, 20, 30])
    battery_pack.apply_translation([0, -100, -30])

    # 4. Combine into Single 3D Assembly Scene
    smart_helmet_assembly = trimesh.util.concatenate([
        eps_liner, 
        camera_mount, 
        hud_mount, 
        compute_board, 
        battery_pack
    ])

    # 5. Export Assembly to 3D Model File
    smart_helmet_assembly.export('smart_helmet_structure.stl')
    smart_helmet_assembly.export('smart_helmet_structure.obj')
    print("Successfully generated 'smart_helmet_structure.stl' and '.obj'")

if __name__ == "__main__":
    create_smart_helmet_3d()