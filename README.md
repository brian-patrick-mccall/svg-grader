# svg-grader
Read patterns from an SVG file into XLSX for grading. Also display graded patterns in Matplotlib and save back to SVG.

## Installation
1. Clone or download the repository.
2. `cd` into the directory.
3. Run `python setup.py install`

## Basic Operation

#### Available commands
```
usage: grade.py [-h] {convert_sample,show_grades,save_grades} ...

Grade an input pattern.

positional arguments:
  {convert_sample,show_grades,save_grades}
                        TODO: Add help statement here.
    convert_sample      Read sample pattern from SVG file.
    show_grades         Show the current graded versions of the sample
                        pattern.
    save_grades         Save graded patterns to a directory.
```

#### Convert sample
```
usage: grade.py convert_sample [-h] input output

positional arguments:
  input       Path to the input pattern.
  output      Path to the excel file (a ".dat" file will also be created in
              the same location).
```

#### Show grades
```
usage: grade.py show_grades [-h] input

positional arguments:
  input       Path to the excel file containing the graded patterns.
```

#### Save grades
```
usage: grade.py save_grades [-h] input output

positional arguments:
  input       Path to the excel file that contains the graded patterns. There
              must also be a ".dat" file in the same location.
  output      Path to a directory (must not exist yet) where to save the
              graded patterns.
```
