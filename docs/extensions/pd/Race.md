---
search:
  boost: 10.0
---

# Class: Race 


_Information about race or racial history_



<div data-search-exclude markdown="1">



URI: [pd:Race](https://w3id.org/lmodel/dpv/pd/Race)





```mermaid
 classDiagram
    class Race
    click Race href "../Race/"
      Ethnicity <|-- Race
        click Ethnicity href "../Ethnicity/"
      
      
```





## Inheritance
* **Race** [ [Ethnicity](Ethnicity.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Race](https://w3id.org/lmodel/dpv/pd/Race) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Race




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Race |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Race |
| native | pd:Race |
| exact | dpv_pd:Race, dpv_pd_owl:Race |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Race
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Race
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about race or racial history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Race
exact_mappings:
- dpv_pd:Race
- dpv_pd_owl:Race
mixins:
- Ethnicity
class_uri: pd:Race

```
</details>

### Induced

<details>
```yaml
name: Race
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Race
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about race or racial history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Race
exact_mappings:
- dpv_pd:Race
- dpv_pd_owl:Race
mixins:
- Ethnicity
class_uri: pd:Race

```
</details></div>