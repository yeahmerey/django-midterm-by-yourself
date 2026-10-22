
from django.contrib.admin import ModelAdmin, register
from django.http import HttpRequest

from apps.categories.models import Category


@register(Category)
class CategoryAdmin(ModelAdmin):
    """Category model admin configuration."""
#Columns in Admin panel 
    list_display = (
        "id",
        "name",
        "slug",
        "description_preview",
    )
#кликабельный столбьцы Clickable columns , Django откроет URL: 
#/admin/categories/category/1/change
#На этой странице Django показывает форму редактирование выбранной категории. 
    list_display_links = (
        "id",
        "name",
    )
#фильтрация между объектами , но тут необходимость нет так как тут используется фильтр типа : 
#когда нажимаешь на какой та name , выходить все объекты который имя = name .  
    list_filter = (
        "name",
    )


#поиск , этот параметр добавляет поиск для удобства чисел =id хорошо , в этом случае ищет будут точное совпадение.
# без =id типо если мы искали 1 и у какого то объекта есть число в нем то дает ошибку
    search_fields = (
        "id",
        "name",
        "slug",
        "description",
    )
#никто не сможет его изменить через форму Django Admin
    readonly_fields = (
        "id",
    )
#какие поля будут показаны в странице создании и также редактирование объекта будет в каком порядке
    fields = (
        "id",
        "name",
        "slug",
        "description",
    )
#при открытие листа тут будет отсортировка по алфавитном порядке , если в обратном порядке надо то использовать надо -name
    ordering = (
        "name",
    )
#показывает до 25 объекта на одном странице
    list_per_page = 25
#когда нажимаешь на show all тут отображается до 100 объектов
    list_max_show_all = 100
#для пустых значение используется - 
    empty_value_display = "—"
#автоматический заполнение slug
    prepopulated_fields = {
        "slug": ("name",),
    }
#кнопка сохранение на верху
    save_on_top = True
#тут позволяет дать количество результатов , то есть это создает нагрузку к системе. 

    show_full_result_count = True
#staticmethod - значит функция не получает автомтический экземпляр CategoryAdmin ему нужен только объект категории obj 
    @staticmethod
    def description_preview(obj: Category) -> str:
        """Return a short description for the list page."""
        if not obj.description:
            return "—"

        if len(obj.description) > 60:
            return f"{obj.description[:60]}..."

        return obj.description

    description_preview.short_description = "Description"


#динамическая настройка доступа к полям
#Этот метод позволяет определять поля только для чтения динамически — в зависимости от того,
#создаётся объект или редактируется существующий.
#Когда создаешь новую категории None, тут уже менять id нельзя но нельзя slug можно , а после сохранение slug , это становиться только для чтение. 

    def get_readonly_fields(
        self,
        request: HttpRequest,
        obj: Category | None = None,
    ) -> tuple[str, ...]:
        """Make the slug read-only after the object is created."""
        if obj:
            return self.readonly_fields + ("slug",)

        return self.readonly_fields