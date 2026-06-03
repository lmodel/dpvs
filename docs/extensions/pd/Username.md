---
search:
  boost: 10.0
---

# Class: Username 


_Information about usernames_



<div data-search-exclude markdown="1">



URI: [pd:Username](https://w3id.org/lmodel/dpv/pd/Username)





```mermaid
 classDiagram
    class Username
    click Username href "../Username/"
      Identifying <|-- Username
        click Identifying href "../Identifying/"
      
      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * **Username**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Username](https://w3id.org/lmodel/dpv/pd/Username) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Username




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Username |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Username |
| native | pd:Username |
| exact | dpv_pd:Username, dpv_pd_owl:Username |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Username
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Username
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about usernames
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Username
exact_mappings:
- dpv_pd:Username
- dpv_pd_owl:Username
is_a: Identifying
class_uri: pd:Username

```
</details>

### Induced

<details>
```yaml
name: Username
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Username
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about usernames
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Username
exact_mappings:
- dpv_pd:Username
- dpv_pd_owl:Username
is_a: Identifying
class_uri: pd:Username

```
</details></div>