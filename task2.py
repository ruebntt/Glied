import sys

def read_circle('https://docs.google.com/document/d/1hi5h5p3QcPlL9IHbVNHst6-B0Y1kFssH/edit'):
    with open('https://docs.google.com/document/d/1hi5h5p3QcPlL9IHbVNHst6-B0Y1kFssH/edit', 'r') as f:
        line = f.readline().strip()
        parts = line.split()
        if len(parts) != 3:
            raise ValueError("Некорректный формат файла окружности.")
        x_center = float(parts[0])
        y_center = float(parts[1])
        radius = float(parts[2])
    return x_center, y_center, radius

def read_points('https://docs.google.com/document/d/1hi5h5p3QcPlL9IHbVNHst6-B0Y1kFssH/edit'):
    points = []
    with open('https://docs.google.com/document/d/1hi5h5p3QcPlL9IHbVNHst6-B0Y1kFssH/edit', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) != 2:
                    continue 
                x = float(parts[0])
                y = float(parts[1])
                points.append((x, y))
    return points

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл_окружности> <файл_точек>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    x0, y0, r = read_circle(circle_file)
    points = read_points(points_file)

    for (x, y) in points:
        dist_sq = (x - x0) ** 2 + (y - y0) ** 2
        r_sq = r ** 2

        epsilon = 1e-12
        if abs(dist_sq - r_sq) < epsilon:
            print(0)
        elif dist_sq < r_sq:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()
