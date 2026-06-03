---
search:
  boost: 10.0
---

# Class: InputData 


_Data that is provided an input to a technology_



<div data-search-exclude markdown="1">



URI: [tech:InputData](https://w3id.org/lmodel/dpv/tech/InputData)





```mermaid
 classDiagram
    class InputData
    click InputData href "../InputData/"
      Input <|-- InputData
        click Input href "../Input/"
      
      
```





## Inheritance
* **InputData** [ [Input](Input.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:InputData](https://w3id.org/lmodel/dpv/tech/InputData) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Input Data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#InputData |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:InputData |
| native | tech:InputData |
| exact | dpv_tech:InputData, dpv_tech_owl:InputData |
| close | iso22989:Data |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#InputData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Data that is provided an input to a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Input Data
exact_mappings:
- dpv_tech:InputData
- dpv_tech_owl:InputData
close_mappings:
- iso22989:Data
mixins:
- Input
class_uri: tech:InputData

```
</details>

### Induced

<details>
```yaml
name: InputData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#InputData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Data that is provided an input to a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Input Data
exact_mappings:
- dpv_tech:InputData
- dpv_tech_owl:InputData
close_mappings:
- iso22989:Data
mixins:
- Input
class_uri: tech:InputData

```
</details></div>