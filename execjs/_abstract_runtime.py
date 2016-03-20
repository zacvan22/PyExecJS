import execjs
from abc import ABCMeta, abstractmethod
import six


@six.add_metaclass(ABCMeta)
class AbstractRuntime(object):
    '''
    Abstract base class for runtime class.
    '''
    def exec_(self, source, cwd=None):
        '''Execute source by JavaScript runtime and return all output to stdout as a string.

        source -- JavaScript code to execute.
        cwd -- Directory where call JavaScript runtime. It may be ignored for some runtime.
        '''
        if not self.is_available():
            raise execjs.RuntimeUnavailableError
        return self._exec_(source, cwd=cwd)

    def eval(self, source, cwd=None):
        '''Evaluate source in JavaScript runtime.

        source -- JavaScript code to evaluate.
        cwd -- Directory where call JavaScript runtime. It may be ignored for some runtime.
        '''
        if not self.is_available():
            raise execjs.RuntimeUnavailableError
        return self._eval(source, cwd=cwd)

    def compile(self, source, cwd=None):
        '''Bulk source as a context object. The source can be used to execute another code.

        source -- JavaScript code to bulk.
        cwd -- Directory where call JavaScript runtime. It may be ignored for some runtime.
        '''
        if not self.is_available():
            raise execjs.RuntimeUnavailableError
        return self._compile(source, cwd=cwd)

    @abstractmethod
    def is_available(self):
        raise NotImplementedError

    @abstractmethod
    def _exec_(self, source, cwd=None):
        raise NotImplementedError

    @abstractmethod
    def _compile(self, source, cwd=None):
        raise NotImplementedError

    @abstractmethod
    def _eval(self, source, cwd=None):
        raise NotImplementedError
