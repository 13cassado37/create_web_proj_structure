import os


# TODO: Разбить программу на функции


normalize_cdn_link = 'https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css'

html_structure = f'<!DOCTYPE html>\n' \
    '<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n' \
    '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' \
    f'\t<title>Document</title>\n\t<link rel="stylesheet" href="{normalize_cdn_link}">\n</head>\n<body>\n\t\n</body>\n</html>\n'

def valid_project_name(project_names):
    ...

def create_file_structure(project_name):
    ...

def main():
    project_name = input('Project name: ')

    existing_projects = [dir for dir in os.listdir() if os.path.isdir(dir)]  # list of numbers and names of projects in directory

    project_numbers = [project.split('_')[0] for project in existing_projects] 
    project_names = [project.split('_')[1] for project in existing_projects]
    
    if project_name in project_names:
        create = input(f'{project_name} already exists, are you sure you want to create project with same name? (Y/n): ').lower()

        if create == '' or create == 'y':
            print('Building new project...')
        elif create == 'n':
            create_new_name = input('Do you want to create project with new name? (Y/n): ')
        else:
            print('Enter')
            

    last_project_number = int(max(project_numbers))
    project_number = str(last_project_number + 1).rjust(3, '0')

    current_proj_name = f'{project_number}_{project_name}'

    os.mkdir(current_proj_name)  # root of the project
    os.mkdir(f'{current_proj_name}/Source')
    os.mkdir(f'{current_proj_name}/{project_name}')
    

    os.mkdir(f'{current_proj_name}/{project_name}/styles')
    os.mkdir(f'{current_proj_name}/{project_name}/js')
    os.mkdir(f'{current_proj_name}/{project_name}/images')
    os.mkdir(f'{current_proj_name}/{project_name}/fonts')

    with open(f'{current_proj_name}/{project_name}/index.html', 'wt') as html:
        html.write(html_structure)
    
    print('Project was built.')

if __name__ == '__main__':
    main()