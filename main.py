from grades import calculate_average
from rich.console import Console
from rich.panel import Panel

def main():
    console = Console()
    
    console.print("[bold cyan]Hello to the Average Grades Calculator[/bold cyan]\n")
    
    grades_list = []
    
    while True:
        user_input = input("Insert grade (To exit press 'q'): ")
        
        if user_input.lower() == 'q':
            break
            
        try:
            grade = float(user_input)
            if 0 <= grade <= 100:
                grades_list.append(grade)
            else:
                console.print("[red]Wrong grade. Insert a grade between 0-100.[/red]")
        except ValueError:
            console.print("[red]Wrong input. Insert a grade between 0-100 or press 'q' to exit[/red]")
            
    if len(grades_list) > 0:
        avg = calculate_average(grades_list)
        
        result_text = f"[bold green]Given grades:[/bold green] {grades_list}\n[bold yellow]Final average:[/bold yellow] [bold mgenta]{avg:.2f}[/bold mgenta]"
        
        panel = Panel(
            result_text, 
            title="[bold blue]Average calculation result[/bold blue]", 
            expand=False,
            border_style="cyan"
        )
        
        console.print("\n")
        console.print(panel)
    else:
        console.print("[yellow]No grades given. Goodbye![/yellow]")

if __name__ == "__main__":
    main()
