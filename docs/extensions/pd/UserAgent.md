---
search:
  boost: 10.0
---

# Class: UserAgent 


_Information about software acting on behalf of users e.g. web browser_



<div data-search-exclude markdown="1">



URI: [pd:UserAgent](https://w3id.org/lmodel/dpv/pd/UserAgent)





```mermaid
 classDiagram
    class UserAgent
    click UserAgent href "../UserAgent/"
      Tracking <|-- UserAgent
        click Tracking href "../Tracking/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * **UserAgent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:UserAgent](https://w3id.org/lmodel/dpv/pd/UserAgent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* User agent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#UserAgent |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:UserAgent |
| native | pd:UserAgent |
| exact | dpv_pd:UserAgent, dpv_pd_owl:UserAgent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UserAgent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#UserAgent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about software acting on behalf of users e.g. web browser
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- User agent
exact_mappings:
- dpv_pd:UserAgent
- dpv_pd_owl:UserAgent
is_a: Tracking
class_uri: pd:UserAgent

```
</details>

### Induced

<details>
```yaml
name: UserAgent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#UserAgent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about software acting on behalf of users e.g. web browser
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- User agent
exact_mappings:
- dpv_pd:UserAgent
- dpv_pd_owl:UserAgent
is_a: Tracking
class_uri: pd:UserAgent

```
</details></div>