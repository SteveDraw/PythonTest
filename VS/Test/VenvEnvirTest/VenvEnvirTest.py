import open3d as o3d
import numpy as np

mesh = o3d.geometry.TriangleMesh.create_box()
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])

# 创建一个 Nx3 的 numpy 点云数组
points = np.random.rand(1000, 3)

# 转为 Open3D 点云对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

o3d.visualization.draw_geometries([pcd])

print(o3d.__version__)