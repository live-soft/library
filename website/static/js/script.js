class Lybrary {
    constructor() {
        this.bookId = null;
        this.interval = null;
        this.timer = null;

        $('.date-picker').datepicker({
            format: 'yyyy/mm/dd',
        });

        this.events();

        setTimeout(() => {
            $('.error-message').removeClass('op');
        }, 5000)
    }

    clearValues() {
        $('.students').val('');
        $('.date-picker input').val('');
    }
    
    eventBinding(event, element, callback) {
        $(document).on(event, element, callback);
    }

    searchBook(e) {
        if (this.interval) {
            clearTimeout(this.interval);
        }

        this.interval = setTimeout(() => {
            $('.search-block .search-btn').trigger('click');
        }, 500)
    }

    async removeAttr() {
        if ($('.students-list form').length > 0) {
            $('.new-student-btn').removeAttr('data-bs-toggle');
            $('.new-student-btn').removeAttr('data-bs-target');
    
            if (this.interval) {
                clearTimeout(this.interval);
            }
    
            this.interval = setTimeout(async () => {
                $('.students-list').addClass('d-none');
    
                if (this.interval) {
                    clearTimeout(this.interval);
                }
    
                if (this.timer) {
                    clearTimeout(this.timer);
                }
    
                await this.secCount();
            }, 5000)
        } else {
            $('.new-student-btn').attr('data-bs-toggle', 'modal');
            $('.new-student-btn').attr('data-bs-target', '#new_student_modal');
        }
    }

    async secCount() {
        for (let i = 5; i >= 0; i--) {
            await this.actionTimer(i);
        }
    }

    async addAttr() {
        if ($('.students-list form').length > 0) {
            $('.timer').html('<div class="loader">Loading...</div>');
    
            $('.new-student-btn').attr('data-bs-toggle', 'modal');
            $('.new-student-btn').attr('data-bs-target', '#new_student_modal');
            $('.students-list').removeClass('d-none');
    
            if (this.timer) {
                clearTimeout(this.timer);
            }
    
            await this.secCount();
        } else {
            $('.students-list').addClass('d-none');
        }
    }

    actionTimer(i) {
        return new Promise(resolve => {
            this.timer = setTimeout(() => {
                if ( i == 0) {
                    resolve($('.timer').html('<div class="loader">Loading...</div>'));
                } else {
                    resolve($('.timer').html(`<center style="color:#fff">${ i }</center>`));
                }
            }, 1000)
        })
    }

    events() {
        this.eventBinding('click', '.assign-btn', this.clearValues.bind(this));
        this.eventBinding('keyup', '.search-box', this.searchBook.bind(this));
        this.eventBinding('mouseenter', '.new-student-btn', this.addAttr.bind(this));
        this.eventBinding('mouseout', '.new-student-btn', this.removeAttr.bind(this));
        this.eventBinding('mouseleave', '.new-student-btn', this.removeAttr.bind(this));
    }
}

new Lybrary();