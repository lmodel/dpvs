---
search:
  boost: 10.0
---

# Class: ContextAwareRetrieval 


_Capability for retrieval of information that takes into account the_

_user's context such as e.g., location, time, device, or activity to_

_provide more relevant results_



<div data-search-exclude markdown="1">



URI: [ai:ContextAwareRetrieval](https://w3id.org/lmodel/dpv/ai/ContextAwareRetrieval)





```mermaid
 classDiagram
    class ContextAwareRetrieval
    click ContextAwareRetrieval href "../ContextAwareRetrieval/"
      Capability <|-- ContextAwareRetrieval
        click Capability href "../Capability/"
      InformationRetrieval <|-- ContextAwareRetrieval
        click InformationRetrieval href "../InformationRetrieval/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [InformationRetrieval](InformationRetrieval.md)
            * **ContextAwareRetrieval** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ContextAwareRetrieval](https://w3id.org/lmodel/dpv/ai/ContextAwareRetrieval) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Context-aware Retrieval




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ContextAwareRetrieval |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ContextAwareRetrieval |
| native | ai:ContextAwareRetrieval |
| exact | dpv_ai:ContextAwareRetrieval, dpv_ai_owl:ContextAwareRetrieval |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContextAwareRetrieval
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ContextAwareRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieval of information that takes into account the

  user''s context such as e.g., location, time, device, or activity to

  provide more relevant results'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Context-aware Retrieval
exact_mappings:
- dpv_ai:ContextAwareRetrieval
- dpv_ai_owl:ContextAwareRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:ContextAwareRetrieval

```
</details>

### Induced

<details>
```yaml
name: ContextAwareRetrieval
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ContextAwareRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieval of information that takes into account the

  user''s context such as e.g., location, time, device, or activity to

  provide more relevant results'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Context-aware Retrieval
exact_mappings:
- dpv_ai:ContextAwareRetrieval
- dpv_ai_owl:ContextAwareRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:ContextAwareRetrieval

```
</details></div>