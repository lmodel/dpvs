---
search:
  boost: 10.0
---

# Class: DialogueManagement 


_Capability for shortening a portion of content such as text while_

_retaining important semantic information_



<div data-search-exclude markdown="1">



URI: [ai:DialogueManagement](https://w3id.org/lmodel/dpv/ai/DialogueManagement)





```mermaid
 classDiagram
    class DialogueManagement
    click DialogueManagement href "../DialogueManagement/"
      Capability <|-- DialogueManagement
        click Capability href "../Capability/"
      LanguageCapability <|-- DialogueManagement
        click LanguageCapability href "../LanguageCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [LanguageCapability](LanguageCapability.md)
            * **DialogueManagement** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DialogueManagement](https://w3id.org/lmodel/dpv/ai/DialogueManagement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Dialogue Management




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.6.14 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DialogueManagement |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DialogueManagement |
| native | ai:DialogueManagement |
| exact | dpv_ai:DialogueManagement, dpv_ai_owl:DialogueManagement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DialogueManagement
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.14
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DialogueManagement
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for shortening a portion of content such as text while

  retaining important semantic information'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Dialogue Management
exact_mappings:
- dpv_ai:DialogueManagement
- dpv_ai_owl:DialogueManagement
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:DialogueManagement

```
</details>

### Induced

<details>
```yaml
name: DialogueManagement
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.6.14
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DialogueManagement
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for shortening a portion of content such as text while

  retaining important semantic information'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Dialogue Management
exact_mappings:
- dpv_ai:DialogueManagement
- dpv_ai_owl:DialogueManagement
is_a: LanguageCapability
mixins:
- Capability
class_uri: ai:DialogueManagement

```
</details></div>