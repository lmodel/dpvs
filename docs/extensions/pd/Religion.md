---
search:
  boost: 10.0
---

# Class: Religion 


_Information about religion, religious inclinations, and religious_

_history._



<div data-search-exclude markdown="1">



URI: [pd:Religion](https://w3id.org/lmodel/dpv/pd/Religion)





```mermaid
 classDiagram
    class Religion
    click Religion href "../Religion/"
      PublicLife <|-- Religion
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* **Religion** [ [PublicLife](PublicLife.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Religion](https://w3id.org/lmodel/dpv/pd/Religion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Religion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Religion |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Religion |
| native | pd:Religion |
| exact | dpv_pd:Religion, dpv_pd_owl:Religion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Religion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Religion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about religion, religious inclinations, and religious

  history.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Religion
exact_mappings:
- dpv_pd:Religion
- dpv_pd_owl:Religion
mixins:
- PublicLife
class_uri: pd:Religion

```
</details>

### Induced

<details>
```yaml
name: Religion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Religion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about religion, religious inclinations, and religious

  history.'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Religion
exact_mappings:
- dpv_pd:Religion
- dpv_pd_owl:Religion
mixins:
- PublicLife
class_uri: pd:Religion

```
</details></div>