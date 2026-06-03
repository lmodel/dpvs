---
search:
  boost: 10.0
---

# Class: ContentBasedRetrieval 


_Capability for retrieval of information using the actual content to_

_identify, select, filter, and provide results_



<div data-search-exclude markdown="1">



URI: [ai:ContentBasedRetrieval](https://w3id.org/lmodel/dpv/ai/ContentBasedRetrieval)





```mermaid
 classDiagram
    class ContentBasedRetrieval
    click ContentBasedRetrieval href "../ContentBasedRetrieval/"
      Capability <|-- ContentBasedRetrieval
        click Capability href "../Capability/"
      InformationRetrieval <|-- ContentBasedRetrieval
        click InformationRetrieval href "../InformationRetrieval/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [InformationRetrieval](InformationRetrieval.md)
            * **ContentBasedRetrieval** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ContentBasedRetrieval](https://w3id.org/lmodel/dpv/ai/ContentBasedRetrieval) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Content-based Retrieval




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ContentBasedRetrieval |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ContentBasedRetrieval |
| native | ai:ContentBasedRetrieval |
| exact | dpv_ai:ContentBasedRetrieval, dpv_ai_owl:ContentBasedRetrieval |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContentBasedRetrieval
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ContentBasedRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieval of information using the actual content to

  identify, select, filter, and provide results'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Content-based Retrieval
exact_mappings:
- dpv_ai:ContentBasedRetrieval
- dpv_ai_owl:ContentBasedRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:ContentBasedRetrieval

```
</details>

### Induced

<details>
```yaml
name: ContentBasedRetrieval
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ContentBasedRetrieval
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability for retrieval of information using the actual content to

  identify, select, filter, and provide results'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Content-based Retrieval
exact_mappings:
- dpv_ai:ContentBasedRetrieval
- dpv_ai_owl:ContentBasedRetrieval
is_a: InformationRetrieval
mixins:
- Capability
class_uri: ai:ContentBasedRetrieval

```
</details></div>