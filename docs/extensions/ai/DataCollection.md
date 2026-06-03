---
search:
  boost: 10.0
---

# Class: DataCollection 


_Processing operation where data is collected, e.g. in a raw or unrefined_

_form_



<div data-search-exclude markdown="1">



URI: [ai:DataCollection](https://w3id.org/lmodel/dpv/ai/DataCollection)





```mermaid
 classDiagram
    class DataCollection
    click DataCollection href "../DataCollection/"
      DataOperation <|-- DataCollection
        click DataOperation href "../DataOperation/"
      
      
```





## Inheritance
* [DataOperation](DataOperation.md)
    * **DataCollection**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataCollection](https://w3id.org/lmodel/dpv/ai/DataCollection) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Collection




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataCollection |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataCollection |
| native | ai:DataCollection |
| exact | dpv_ai:DataCollection, dpv_ai_owl:DataCollection |
| close | iso42001:DataResource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataCollection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataCollection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is collected, e.g. in a raw or unrefined

  form'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Collection
exact_mappings:
- dpv_ai:DataCollection
- dpv_ai_owl:DataCollection
close_mappings:
- iso42001:DataResource
is_a: DataOperation
class_uri: ai:DataCollection

```
</details>

### Induced

<details>
```yaml
name: DataCollection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataCollection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is collected, e.g. in a raw or unrefined

  form'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Collection
exact_mappings:
- dpv_ai:DataCollection
- dpv_ai_owl:DataCollection
close_mappings:
- iso42001:DataResource
is_a: DataOperation
class_uri: ai:DataCollection

```
</details></div>